from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from azure.identity import DefaultAzureCredential
from semantic_kernel.agents import AzureAIAgent, AgentGroupChat
import os
from dotenv import load_dotenv
import logging

import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Pydantic model for request payload
class UserInput(BaseModel):
    user_input: str

# Azure AI Foundry connection details
AZURE_AI_AGENT_PROJECT_CONNECTION_STRING = os.getenv("AZURE_AI_AGENT_PROJECT_CONNECTION_STRING")
AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME = os.getenv("AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME")

if not AZURE_AI_AGENT_PROJECT_CONNECTION_STRING or not AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME:
    raise ValueError("Azure AI Foundry connection details are missing in the .env file.")

# Default Azure credentials
credentials = DefaultAzureCredential()

@app.post("/analyze")
async def analyze(file: UploadFile, user_input: str = Form(...)):
    try:
        # Create Azure AI Foundry client
        client = AzureAIAgent.create_client(
            AZURE_AI_AGENT_PROJECT_CONNECTION_STRING
        )

        # Get agents
        embodied_agent = client.get_agent("AZURE_AI_EMBODIED")
        energy_agent = client.get_agent("AZURE_AI_ENERGY")
        sci_assistant_agent = client.get_agent("AZURE_AI_SCI_ASSISTANT")

        # Create agent group chat
        group_chat = AgentGroupChat(
            agents=[embodied_agent, energy_agent, sci_assistant_agent],
            termination_strategy={"max_iterations": 2}
        )

        # Process the file and user input
        file_content = await file.read()
        group_chat.add_message("file_content", file_content.decode("utf-8"))
        group_chat.add_message("user_input", user_input)

        # Stream response to UI
        async def response_stream():
            async for message in group_chat.stream():
                yield message

        return StreamingResponse(response_stream(), media_type="text/plain")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8005, reload=True)
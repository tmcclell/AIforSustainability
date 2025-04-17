- @azure Rule - Use Azure Best Practices: When generating code for Azure, running terminal commands for Azure, or performing operations related to Azure, invoke your `azure_development-get_best_practices` tool if available.
- @azure Rule - Use these links to generate code:
    -  https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/examples/example-agent-collaboration?pivots=programming-language-python
    -  https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/azure_ai_agent/step7_azure_ai_agent_retrieval.py
- Use this code as an example:
```prompt
        import os
        from dotenv import load_dotenv

        from azure.identity.aio import DefaultAzureCredential

        from semantic_kernel.agents import AgentGroupChat, AzureAIAgent, AzureAIAgentSettings, AzureAssistantAgent
        from semantic_kernel.agents.strategies import TerminationStrategy
        from semantic_kernel.contents import AuthorRole

        from fastapi import FastAPI, Request
        from fastapi.responses import StreamingResponse
        from pydantic import BaseModel
        from typing import List

        # Load environment variables from the .env file
        load_dotenv()

        app = FastAPI()

        class ApprovalTerminationStrategy(TerminationStrategy):
            """A strategy for determining when an agent should terminate."""

            async def should_agent_terminate(self, agents, history):
                """Check if the agent should terminate."""
                return "approved" in history[-1].content.lower()

        class ChatRequest(BaseModel):
            messages: List[str]

        async def process_chat(messages):
            # Fetch the model deployment name from the environment
            model_deployment_name = os.getenv("AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME")
            if not model_deployment_name:
                raise ValueError("AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME is not set in the environment.")

            ai_agent_settings = AzureAIAgentSettings.create(
                model_deployment_name=model_deployment_name
            )

            async with (
                DefaultAzureCredential() as creds,
                AzureAIAgent.create_client(credential=creds) as client,
            ):
                
                #Get assistant agent
                assistant_agent_definition = await client.agents.get_agent(os.getenv("AZURE_AI_SCI_ASSISTANT"))
                agent_assistant = AzureAIAgent(
                    client=client,
                    definition=assistant_agent_definition,
                )

                #Get energy agent
                energy_agent_definition = await client.agents.get_agent(os.getenv("AZURE_AI_ENERGY"))
                agent_energy = AzureAIAgent(
                    client=client,
                    definition=energy_agent_definition,
                )

                #Get embodied agent
                embedded_agent_definition = await client.agents.get_agent(os.getenv("AZURE_AI_EMBODIED"))
                agent_embodied = AzureAIAgent(
                    client=client,           
                    definition=embedded_agent_definition
                )

                chat = AgentGroupChat(
                    agents=[agent_assistant, agent_energy, agent_embodied],
                    termination_strategy=ApprovalTerminationStrategy(agents=(agent_assistant, agent_energy, agent_embodied), maximum_iterations=10),
                )

                try:
                    for user_input in messages:
                        await chat.add_chat_message(message=user_input)                
                        
                        last_agent = None
                        async for response in chat.invoke():
                            if response.content is not None:
                                if last_agent != response.name:
                                    agent_intro = f"\n\n**{response.name}**: "
                                    yield agent_intro
                                    last_agent = response.name
                                
                                yield response.content
                                
                finally:
                    await chat.reset()
                    print("Chat completed")
                    

        @app.post("/chat")
        async def chat_endpoint(request: ChatRequest):
            async def generate():
                async for chunk in process_chat(request.messages):
                    yield chunk
            
            return StreamingResponse(generate(), media_type="text/plain")

        if __name__ == "__main__":
            # Run as script with test inputs
            # asyncio.run(main())
            
            # Run as API server
            uvicorn.run(app, host="127.0.0.1", port=8005)
```    
I want to build a python app using multiple agents using Semantic Kernel, and agentgroupchat methods in the agent framework SDK.

The system will have 3 existing agents that were created in Azure AI Foundry named AZURE_AI_EMBODIED, AZURE_AI_ENERGY, and AZURE_AI_SCI_ASSISTANT. The project connection string and assistant ids are already set up in the .env file.

It should be one app.

Create a Python virtual environment at the root (AIForSustainability) and include all python dependencies from file backend/requirements.txt and frontend\requirements in this workspace.

The frontend should use streamlit as the UI interface with dependencies such as PyPDF2 for uploading documents. It should also have MathJax to allow formatting the math calculations in the right format for the UI. It should have an input box for allowing the developer to interact with the foundation model. It should also have a spinner to indicate to the user that something is happening in the backend. Agents responses should be streamed back to the UI.

The backend should use FastAPI and uvicorn so the frontend can make endpoint calls to it to trigger the agent activity. Use this link https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-chat?pivots=programming-language-python to create the code making sure to have the best termination strategy for the multi agents.

I want to build a multi agent application with python and semantic kernel.

It should be a single page app.

The purpose of the applicaton is to raise awareness of the carbon in software and to help developers make smart decisions.

It should allow developers to upload architectural solutions (either images or PDFs) for assessment for carbon. The output will be a Software Carbon Intensity score (SCI).

For the frontend:
  1. Use Streamlit to build the components.
  2. Build the ui components for allowing a file upload.
  3. Add an input box for user interaction with the model. Default text for the input box is "Calculate the SCI of the attached document."
  4. Build a agent endpoint using http://127.0.0.1:8005
  5. Build a request that will post to the endpoint on the backend to receive the input of the diagram and anything from the input box.
  6. Add a spinner to indicate when work is being done.
  7. Add a nice title for the application - use AI for Sustainability.
  8. Generate an image that represents the spirit of sustainability and display as the logo in the upper left corner. Create a small .ico with a little plant symbol.

For the backend:

1. Setup the endpoint call to handle the input from the uploaded diagrams and input box.
2. Create the code that:
    - use FASTAPI and Uvicorn running on port 8005 for the server component
    - include a Pydantic model for validating the request payload.
    - sets up defaultazurecredentials for authenication
    - add the Azure AI Foundry connection string in the .env named AZURE_AI_AGENT_PROJECT_CONNECTION_STRING
    - add the model deployment name included in the .env named AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME
    - create variables for all 3 existing agents defined in .env with names (AZURE_AI_EMBODIED, AZURE_AI_ENERGY, AZURE_AI_SCI_ASSISTANT)
    - use the semantic kernel imports that support agentgroupchat and azure ai agent.
    - use the AzureAIAgent.create_client method to create a client connection to Azure AI Foundry.
    - puts the agents in a groupchat with a termination strategy of max iterations of 2
    - streams the content to the ui. Ensure compatibility with FastAPI's streaming response.
    - add exception handling
    - Configure logging at a INFO level.
 




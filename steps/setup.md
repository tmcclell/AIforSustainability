### How to use

1. Open all files in the `docs` folder and keep this file open in the editor throughout this exercise.
2. Agent mode uses `application-requirements.md` as a reference to create the application.
3. Copy and paste the following prompt(s) in the GitHub Copilot Chat and select the "Agent" instead of "Ask" or "Edit" from the drop down where you are inserting the prompt.

![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)

```prompt
Let's take the following step by step and generate instructions in this order and execute the commands. Use docs/application-requirements.md as a guide for the project structure and requirements.

1. Understand the story of calculating carbon in software from the docs/green-software-story.md file.
2. All packages have been preinstalled.
3. Verify all packages have been installed. 

Don't proceed with the next activity until all of these steps are completed.
```
❕ **Important:** Once the above activity installs all the required packages, proceed to the next activity.

### :keyboard: Activity: Let's generate the frontend

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
  Based on the example AI for Sustainability app in the docs/application-requirements.md file, let's build the frontend for analysing a pdf or image file, extracting the text components and send the request payload to the backend. Use chat.py for this code.
 
  1. Use Streamlit to build the components.
  2. Build the ui components for allowing a file upload.
  3. Add an input box for user interaction with the model.
  4. Build a agent endpoint using http://127.0.0.1:8005
  5. Build a request that will post to the endpoint on the backend to receive the input of the diagram and anything from the input box.
  6. Add a spinner to indicate when work is being done.
  7. Add a nice title for the application - use AI for Sustainability.
  8. Generate an image that represents the spirit of sustainability and display as the logo in the upper left corner. 

  Don't proceed with the next activity until all of these steps are completed.
 ```

### :keyboard: Activity: Let's generate the backend api

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
  Based on the example AI for Sustainability app in the docs/application-requirements.md file, let's build the api for sending a user request to the agents for evaluation. Use main.py for the backend code.
 
1. Setup the endpoint call to handle the input from the uploaded diagrams and input box.
2. Create the code that:
    - use FASTAPI for the server component
    - include a Pydantic model for validating the request payload.
    - sets up defaultazurecredentials for authenication
    - add the Azure AI Foundry connection string in the .env named AZURE_AI_AGENT_PROJECT_CONNECTION_STRING
    - add the model deployment name included in the .env named AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME
    - use the semantic kernel imports that support agentgroupchat and azure ai agent.
    - use the AzureAIAgent.create_client method to create a client connection to Azure AI Foundry.
    - use the client.get_agent method to get all 3 existing agents (AZURE_AI_EMBODIED, AZURE_AI_ENERGY, AZURE_AI_SCI_ASSISTANT)
    - puts the agents in a groupchat with a termination strategy of max iterations of 2
    - streams the content to the ui. Ensure compatibility with FastAPI's streaming response.
    - add exception handling
 
  Don't proceed with the next activity until all of these steps are completed.
 ```

### :keyboard: Activity: Exception Handling & Logging

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
  Configure logging at a INFO level.
  Review the code is any potential issues.
  
  Don't proceed with the next activity until all of these steps are completed.
 ```

### :keyboard: Activity: Start the frontend and backend services.

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
  Start the backend with uvicorn and have it run on port 8005.
  Wait for the backend to start and then start the frontend.
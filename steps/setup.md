1. Open all files in the `docs` folder and keep this file open in the editor throughout this exercise.
2. Agent mode uses `application-requirements.md` as a reference to create the application.
3. Copy and paste the following prompt(s) in the GitHub Copilot Chat and select the "Agent" instead of "Ask" or "Edit" from the drop down where you are inserting the prompt.

```prompt
Let's take the following step by step and generate instructions in this order and execute the commands.
Use docs/application-requirements.md as a guide for the project structure and requirements.

1. Understand the story of calculating carbon in software from the docs/green-software-story.md file.
2. All packages have been preinstalled.
3. Setup the python virtual environment at the root using both backend/requirements.txt and frontend/requirements.txt.
4. Verify all packages have been installed. 


Don't proceed with the next activity until all of these steps are completed.
```
❕ **Important:** Once the above activity installs all the required packages, proceed to the next activity.

### :keyboard: Activity: Let's generate the frontend

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
  Based on the example AI for Sustainability app in the docs/application-requirements.md file, let's build the frontend for analysing a pdf or image file, extracting the text components and send the request to the backend.
 
  1. Build the ui components for file uploads and an input box for user interaction.
  2. Build a agent endpoint using http://127.0.0.1:8005
  2. Build a request that will post to the endpoint on the backend to receive the input of the diagram.

 
  Don't proceed with the next activity until all of these steps are completed.
 ```

### :keyboard: Activity: Let's generate the backend api

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
  Based on the example AI for Sustainability app in the docs/application-requirements.md file, let's build the api for sending a user request to the agents for evaluation.
 
1. Setup the api call to handle the input from the uploaded diagrams.
2. Create the code that:
    - sets up defaultazurecredentials for authenication
    - gets the existing energy agent
    - gets the existing embodied agent
    - gets the existing assistance agent
    - puts the agents in a groupchat with a termination strategy of max iterations of 2
    - streams the content to the ui.

2. Create the code that connects to the existing agents using the information in the .env.
 
  Don't proceed with the next activity until all of these steps are completed.
 ```
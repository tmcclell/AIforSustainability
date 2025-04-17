### How to use

1. Open all files in the `docs` folder and keep this file open in the editor throughout this exercise.
2. Agent mode uses `application-requirements.md` as a reference to create the application.
3. Copy and paste the following prompt(s) in the GitHub Copilot Chat and select the "Agent" instead of "Ask" or "Edit" from the drop down where you are inserting the prompt.

![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)

```prompt
Let's take the following step by step and generate instructions in this order and execute the commands. Use docs/application-requirements.md as a guide for the project structure and requirements.

1. Understand the story of calculating carbon in software from the docs/green-software-story.md file.
2. Understand the requirements for the application from docs/application-requirements.md
3. Read the .github/copilot-instructions.md

Don't proceed with the next activity until all of these steps are completed.
```

### :keyboard: Activity: Let's generate the frontend

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
  Based on the example AI for Sustainability app in the docs/application-requirements.md file, let's build the frontend for analysing a pdf or image file, extracting the text components and send the request payload to the backend for an SCI calculation. Use chat.py for this code.

  Don't proceed with the next activity until all of these steps are completed.
 ```

### :keyboard: Activity: Let's generate the backend api

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
  Use the information in docs/application-requirements.md file for application requirements, build the endpoint for a multi agent solution. Use main.py for the backend code.

  Don't proceed with the next activity until all of these steps are completed.
 ```

### :keyboard: Activity: Double check the code - react

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
 
  Review the code is any potential issues.
  
  Don't proceed with the next activity until all of these steps are completed.
 ```

### :keyboard: Activity: Start the frontend and backend services.

  ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
 
  ```prompt
  Start the backend with uvicorn and have it run on port 8005.
  Wait for the backend to start and then start the frontend with streamlit.
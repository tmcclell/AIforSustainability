# Building a Sustainability app with GitHub Copilot agent mode for Green Software Foundation.

## AI for Sustainability application story for Green Software Foundation

After Tammy McClellan, a Cloud Solution Architect from Microsoft saw the announcement of the creation of the Green Software Foundation (GSF) in 2022 along with other tech collegues and partners, she immediately knew that this was something she could be passionate about. The GSF vision was to build a trusted ecosystem of people, standards, tooling and best practices for green software. Green software is software that is responsible for emitting fewer greenhouse gases. The focus is on reduction, not neutralisation.

The first order of busiess was to build a standard to calculate carbon in software where the Software Carbon Intensity (SCI) was created.

The SCI was adopted by ISO in 2024 becoming an industry standard.

After creating multiple use cases to demonstrate how to calculate carbon in software and the evolution of genAI," Tammy became inspired to create a solution. She wanted something that would:

1. Allow software architects to have AI analysis a software diagram.
2. Understand the components of the diagram.
3. Allow the developer to observe utilization characteristics of the components in the diagram including CPU and Memory utilization data.
4. Calculate the SCI score for each component of the diagram.
5. Return a final aggregate number for all components of the diagram and return it to the user.
6. Pass recommendations of how to reduce the score back to the user.

### Technical Planning Phase

The solution must connect with agents already existing in Azure AI Foundry named AZURE_AI_EMBODIED, AZURE_AI_ENERGY, AZURE_AI_SCI_ASSISTANT built on gpt4o modern with the latest version.

### User Experience Goals

- Simple, intuitive interface designed specifically for allowing developers to upload documents, both PDF and images.
- Provide accurate and reliable information about potential carbon in software.
- Allow the developer to ask follow up questions.

### Technical Specifications

- Ability to upload diagrams with PDF or image formats.
- Use Python along with Semantic Kernel and agentgroupchat for orchestraing agents results.
- All interaction with the foundational model for follow up questions
- Use a multi agent approach, using agents that have already been created in Azure AI Foundry along with their actions and knowledge.

### Green Foundation Foundation Key Links
The first link explains the SCI and contain use cases that will help you learn. The second link explains patterns, principles, and best practices for reduction.
#### [SCI Explained](https://sci-guide.greensoftware.foundation/)
#### [Patterns](https://patterns.greensoftware.foundation/)

### GitHub Copilot Chat

These are the current models supported for GitHub Copilot Chat.

- Claude Sonnet 3.5 (Preview)
- Claude Sonnet 3.7 (Preview)
- Claude Sonnet 3.7 Thinking (Preview)
- Gemini 2.0 Flash (Preview)
- GPT-4o
- o1 (Preview)
- o3-mini (Preview)

#### [LLM models explained](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-1)

![GitHub Copilot Chat models](https://github.com/user-attachments/assets/f2f8d0bd-366b-4ecf-b88d-d092ae7b8b10)

#### Prompt engineering

- [GitHub documentation prompt engineering](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [How to use GitHub Copilot: Prompts, tips, and use cases](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [Using GitHub Copilot in your IDE: Tips, tricks, and best practices](https://github.blog/2024-03-25-how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)
- [A developer's guide to prompt engineering and LLMs](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot#:~:text=A%20developer%E2%80%99s%20guide%20to%20prompt%20engineering%20and%20LLMs)
- [GitHub Copilot: The Agent Awakens](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/#agent-mode-available-in-preview-%f0%9f%a4%96)

### AI for Sustainability application technology stack

We'll be using a modern web application stack:

- **Frontend**: streamlit
- **Backend**: Python with Semantic Kernel and AgentGroupChat functionality with responses streaming back to the user interface.


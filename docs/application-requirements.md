I want to build a multi agent application with python and semantic kernel.

It should be a single page app.

The purpose of the applicaton is to raise awareness of the carbon in software and to help developers make smart decisions.

It should allow developers to upload architectural solutions (either images or PDFs) for assessment for carbon. The output will be a Software Carbon Intensity score (SCI).

Use the methods defined in this article - https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-chat?pivots=programming-language-python.

Use this as an example for generating the code for calling an agent.

This code snippet demonstrates the initialization and configuration of an Azure AI Agent for a sustainability application. 

1. **Fetch Model Deployment Name**: 
    - Retrieves the model deployment name from the environment variable `AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME`.

2. **Authentication**: 
    - Uses `DefaultAzureCredential` to authenticate with Azure services.

3. **Create Azure AI Agent Client**: 
    - Initializes the Azure AI Agent client using the provided credentials.

4. **Retrieve Agent Definition**: 
    - Fetches the assistant agent definition using the environment variable `AZURE_AI_SCI_ASSISTANT`.

5. **Initialize Azure AI Agent**: 
    - Creates an instance of `AzureAIAgent` using the client and the retrieved agent definition.

6. **Set Up Agent Group Chat**: 
    - Configures a group chat with multiple agents (`agent_assistant`, `agent_energy`, `agent_embodied`).
    - Specifies a termination strategy (`ApprovalTerminationStrategy`) that limits the chat to a maximum of 2 iterations and requires approval from all agents.

7. **Reset Chat State**: 
    - Resets the chat session to ensure a clean state before starting interactions.

Use this block of code as an example

model_deployment_name = os.getenv("AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME")
model_deployment_name=model_deployment_name
ai_agent_settings = AzureAIAgentSettings.create(
    model_deployment_name=model_deployment_name
)
DefaultAzureCredential() as creds,
AzureAIAgent.create_client(credential=creds) as client
assistant_agent_definition = await client.agents.get_agent(os.getenv("AZURE_AI_SCI_ASSISTANT"))
agent_assistant = AzureAIAgent(
    client=client,
    definition=assistant_agent_definition,
)
chat = AgentGroupChat(
    agents=[agent_assistant, agent_energy, agent_embodied],
    termination_strategy=ApprovalTerminationStrategy(agents=(agent_assistant, agent_energy, agent_embodied), maximum_iterations=2),
)
await chat.reset()
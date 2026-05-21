import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

# 1. Configuration Setup
GEMMA_MODEL = os.environ.get("GEMMA_MODEL", "ai/gemma4:e4b")
MODEL_NAME = f"openai/{GEMMA_MODEL}"
BASE_URL = os.environ.get("MODEL_RUNNER_URL", "http://localhost:9000/engines/v1") 

# 2. Define the isolated local model client pointing to Docker Model Runner
local_gemma_model = LiteLlm(
    model=MODEL_NAME,        
    api_key="local_bypass",
    base_url=BASE_URL
)

# 3. Initialize the Local Agent relying purely on Gemma 4's internal intelligence
root_agent = LlmAgent(
    model=local_gemma_model,  # Uses your local container client
    name="root_agent",
    description="Your name is James!! Your job is to help attendees to find places to visit in Hyderabad, India.",
    instruction="Answer user questions to the best of your knowledge. Rely entirely on your internal memory and reasoning capabilities without using external tools.",
    tools=[]  # 🚫 Completely removed all external tools/search integrations
)

# 4. Local testing execution hook
if __name__ == "__main__":
    print(f"🚀 Root Agent 'James' active via offline model: {MODEL_NAME}")
    prompt = "What are the top 3 historical places to visit in Hyderabad?"
    print(f"\n[User]: {prompt}")
    
    response = root_agent.run(prompt)
    print(f"\n[James]: {response}")
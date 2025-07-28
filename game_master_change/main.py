
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from multy_agents import main_agent

# Load the environment variables
load_dotenv()

# Get Gemini API key from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please define it in your .env file.")

# External client using Gemini (via OpenAI-style interface)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Define model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # or gemini-1.5-pro etc.
    openai_client=external_client
)

# Create run config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Run the agent
result = Runner.run_sync(
    main_agent,
    input="I challenge the monster!.",
    run_config=config
)

# Show output
print("\n--- Final Output ---\n")
print(result.final_output)

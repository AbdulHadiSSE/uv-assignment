from os import getenv
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_client,
    set_tracing_disabled,
    OpenAIChatCompletionsModel
) 

load_dotenv()

api_key = getenv("GEMINI_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url
)

set_default_openai_client(external_client)
set_tracing_disabled(True)

my_model = OpenAIChatCompletionsModel(
    model = "gemini-2.5-flash", openai_client=external_client
)

agent =  Agent(
    name="MyGreetingAgent",
    instructions="You are a friendly assistant that greets users warmly.",
    model=my_model
)

def greeting_agent():
    result = Runner.run_sync(
        agent, "Ask user for their name and greet them warmly."
    )
    print(result.final_output)


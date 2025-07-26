from dotenv import load_dotenv 
import os
from agents import Agent , Runner, AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig

load_dotenv()
gemini_api_key =os.getenv("GEMINI_API_KEY")


if not gemini_api_key:
 raise ValueError("GEMINI_API_KEY is not set . please ensure it is defined in .env file" )

external_client:AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#Initialize model
model:OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

language = Agent(
    name = "Translator",
    instructions="your are a helpful translator. Always translate english sentences into clear and simple roman urdu",
)

result =Runner.run_sync(
 language , 
 input ="My name is shereen . i am a software engineer" ,
   run_config=config
)
print(result)


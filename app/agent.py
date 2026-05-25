import os

from dotenv import load_dotenv
from agents import Agent, Runner

from app.prompts import SYSTEM_PROMPT

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

conversion_agent = Agent(
    name="Ecommerce Conversion Agent",
    instructions=SYSTEM_PROMPT,
    model=MODEL,
)


async def run_audit(user_input: str) -> str:
    result = await Runner.run(
        conversion_agent,
        input=user_input,
    )
    return result.final_output

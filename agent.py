import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts import SYSTEM_PROMPT
from tools import build_tools

load_dotenv()

DEFAULT_MODEL = "gemini-2.5-flash"


def build_agent():
    llm = ChatGoogleGenerativeAI(
        model=os.getenv("MODEL") or DEFAULT_MODEL,
        temperature=0,
    )
    return create_agent(llm, tools=build_tools(), system_prompt=SYSTEM_PROMPT)

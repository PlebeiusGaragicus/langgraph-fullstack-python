"""A simple chatbot, made using create_react_agent."""

from typing import Any

from langchain.chat_models import init_chat_model
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import create_react_agent

PROMPT = "You are a friendly, curious, geeky AI."

# Define the function that calls the model


def prompt(
    state: dict[str, list[AnyMessage]], config: RunnableConfig
) -> list[AnyMessage | dict[str, Any]]:
    """Prepare messages for the model."""
    sys_prompt = config["configurable"].get("system_prompt")
    sys_prompt = sys_prompt or PROMPT
    return [{"role": "system", "content": sys_prompt}, *state["messages"]]


llm = init_chat_model("anthropic:claude-3-5-sonnet-latest")
graph = create_react_agent(llm, tools=[], prompt=prompt)  # type: ignore

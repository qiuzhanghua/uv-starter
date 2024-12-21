from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
import asyncio

model = OllamaModel("glm4")
agent = Agent(model=model, system_prompt="你是AI助手,尽量简要回答问题")


async def main():
    result = await agent.run('"hello world"的来源是什么?')
    print(result.data)


asyncio.run(main())

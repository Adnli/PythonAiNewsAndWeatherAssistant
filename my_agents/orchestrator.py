import asyncio
from agents import Agent, Runner
from agents.model_settings import ModelSettings
from my_agents.prompts import SYSTEM_INSTRUCTIONS
from mcp_config.mcp_servers import build_mcp_servers

class WeatherNewsOrchestrator:
    def __init__(self):
        self._mcp_servers = build_mcp_servers()
        self._agent = Agent(
            name="Weather+News Assistant",
            instructions=SYSTEM_INSTRUCTIONS,
            mcp_servers=self._mcp_servers,
            model_settings=ModelSettings(tool_choice="auto"),
        )

    async def _run_once(self, conversation_messages: list[dict[str, str]]) -> str:
        for s in self._mcp_servers:
            await s.__aenter__()
        try:
            user_text = next(m["content"] for m in reversed(conversation_messages) if m["role"] == "user")
            result = await Runner.run(self._agent, user_text, context={"history": conversation_messages})
            return result.final_output
        finally:
            for s in reversed(self._mcp_servers):
                try:
                    await s.__aexit__(None, None, None)
                except Exception:
                    pass

def run_answer(orchestrator: WeatherNewsOrchestrator, messages: list[dict[str, str]]) -> str:
    return asyncio.run(orchestrator._run_once(messages))

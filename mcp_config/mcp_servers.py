import os
from agents.mcp import MCPServerStdio

def build_mcp_servers():
    open_meteo = MCPServerStdio(
        name="open-meteo",
        params={
            "command": "node",
            "args": ["dist/index.js"],
            "cwd": "open-meteo-mcp",
            "timeout": 20,
        },
        cache_tools_list=True,
        max_retry_attempts=2,
    )
    newsnow = MCPServerStdio(
        name="newsnow",
        params={
            "command": "uvx",
            "args": ["mcp-newsnow"],
            "timeout": 20,
        },
        cache_tools_list=True,
        max_retry_attempts=2,
    )
    return [open_meteo, newsnow]

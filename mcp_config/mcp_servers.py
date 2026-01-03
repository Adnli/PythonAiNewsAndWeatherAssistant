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

    rss_news = MCPServerStdio(
        name="rss",
        params={
            "command": "node",
            "args": ["dist/index.js"],
            "cwd": "rss-mcp",
            "timeout": 20,
        },
        cache_tools_list=True,
        max_retry_attempts=2,
    )
    return [open_meteo, rss_news]

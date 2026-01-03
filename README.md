# Weather & News Assistant (Streamlit + MCP)
## Github repository: 
https://github.com/Adnli/PythonAiNewsAndWeatherAssistant
## Youtube demo video:
https://youtu.be/5f3w-23_GmU
## 📖 Overview
A Python-based web application with a chat interface that answers questions about **current weather** and **latest news**.  
The project uses an **agent-based architecture** and **Model Context Protocol (MCP)** to integrate external data sources in a standardized way.
---
## 🚀 Features
- Chat-style web interface (Streamlit)
- Weather questions (via Open-Meteo MCP server)
- News questions (via MCP NewsNow, no API key required)
- Multi-turn conversations (follow-up questions)
- Agent orchestrator with intent routing
- MCP (stdio) for standardized tool integration
---
## 🧱 Tech Stack
- **Python 3.11+** (recommended: 3.11 or 3.12)
- **Streamlit** — web UI
- **OpenAI Agents SDK** — agent orchestration
- **MCP (Model Context Protocol)** — tool integration
- **Node.js** — Open-Meteo MCP server
- **uv / uvx** — NewsNow MCP server
---
## 📁 Project Structure
```bash
project/
├── app.py
├── my_agents/
│ ├── init.py
│ ├── orchestrator.py
│ ├── prompts.py
│ └── state.py
├── mcp_config/
│ ├── init.py
│ └── mcp_servers.py
├── open-meteo-mcp/ # local Open-Meteo MCP server
├── rss-mcp/ # local RSS MCP server
├── requirements.txt
├── README.md
└── .env # not committed to git
```
---
## ✅ Prerequisites
### 1️⃣ Python
- Python **3.11 or 3.12**
- Check version:
```bash
python --version
```
### 2️⃣ Node.js (for Open-Meteo MCP)
- Install Node.js LTS
- Check:
```bash
node -v
npm -v
```
### 3️⃣ Git
```bash
git --version
```

## Installation open-meteo-mcp dependencies:
open-meteo-mcp:
```bash
cd open-meteo-mcp 
npm install
npm run build
cd ..
```
rss-mcp:
```bash
cd rss-mcp
npm install
npm run build
cd ..
```
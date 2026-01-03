import streamlit as st
from my_agents.orchestrator import WeatherNewsOrchestrator, run_answer
from my_agents.state import ChatState
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Weather & News (MCP)", page_icon="🌦️", layout="centered")
st.title("Weather & News Assistant (MCP)")

if "chat" not in st.session_state:
    st.session_state.chat = ChatState()

if "orch" not in st.session_state:
    st.session_state.orch = WeatherNewsOrchestrator()

for msg in st.session_state.chat.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask about weather or news…")
if prompt:
    st.session_state.chat.add_user(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking and fetching data…"):
            try:
                answer = run_answer(st.session_state.orch, st.session_state.chat.messages)
            except Exception as e:
                answer = (
                    "An error occurred while contacting the services.\n\n"
                    f"Error details: `{e}`\n\n"
                    "Please make sure the MCP servers are running "
                    "(Node.js and uv/uvx are installed) and try again."
                )
            st.markdown(answer)

    st.session_state.chat.add_assistant(answer)

import sys

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Add project root to sys.path so Python can find your omniagent package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from omniagent.agent_registry import AGENTS
from omniagent.utils.agent_runner import run_agent_safely
from omniagent.memory.memory_utils import retrieve_similar_prompts

st.set_page_config(page_title="OmniAgent AI", layout="wide")
st.title("🤖 OmniAgent AI — Multi-Agent Reasoning Assistant")
st.caption("Interact with specialized agents powered by DeepSeek + Memory")

# Select agent dropdown
selected_agent_key = st.selectbox("🧠 Choose an Agent", options=list(AGENTS.keys()))
agent = AGENTS[selected_agent_key]

# Show agent info
st.markdown(f"**📝 Description**: {agent.description}")
st.markdown(f"**🔧 Tools**: {', '.join(agent.tools) or 'None'}")
st.markdown(f"**💾 Memory Scope**: `{agent.memory_scope}`")
st.markdown("---")

# Input based on agent input_type
user_input = None
if agent.input_type == "code":
    user_input = st.text_area("💻 Enter your code or question:")
elif agent.input_type == "file":
    uploaded_file = st.file_uploader("📁 Upload a file")
    if uploaded_file:
        user_input = uploaded_file.read().decode("utf-8")
else:
    user_input = st.text_input("🧠 Describe your task:")

# Show relevant memory preview
if user_input:
    memory = retrieve_similar_prompts(user_input)
    if memory:
        with st.expander("🔁 Related Memory Found", expanded=False):
            for i, m in enumerate(memory[:3]):
                st.markdown(f"**#{i+1}**\n```\n{m.strip()}\n```")

# Run agent and show results
result = None
if st.button(f"Run {agent.name}"):
    if not user_input:
        st.warning("Please provide a task or file to process.")
    else:
        with st.spinner("Running agent..."):
            try:
                result = run_agent_safely(agent.name, user_input)
                st.success("✅ Agent completed the task")
                lang = "python" if agent.input_type == "code" else "text"
                st.code(result, language=lang)
            except Exception as e:
                st.error(f"❌ Error while running agent: {e}")

# Feedback mechanism
if agent.learnable and result is not None:
    st.markdown("### 🧠 Was this helpful?")

    # Reset feedback state if agent or input changed
    if 'last_agent' not in st.session_state or st.session_state.last_agent != selected_agent_key:
        st.session_state.feedback_given = False
        st.session_state.last_agent = selected_agent_key

    if 'last_input' not in st.session_state or st.session_state.last_input != user_input:
        st.session_state.feedback_given = False
        st.session_state.last_input = user_input

    if "feedback_given" not in st.session_state:
        st.session_state.feedback_given = False

    if not st.session_state.feedback_given:
        feedback = st.radio("Feedback:", ["👍 Yes", "👎 No"], horizontal=True, key="feedback_radio")
        if st.button("Submit Feedback"):
            if feedback:
                feedback_bool = True if feedback == "👍 Yes" else False
                try:
                    agent.learn(feedback_bool, user_input, result)
                    st.success("📝 Feedback recorded. Thank you!")
                    st.session_state.feedback_given = True
                except Exception as e:
                    st.error(f"❌ Error recording feedback: {e}")
            else:
                st.warning("Please select a feedback option before submitting.")
    else:
        st.info("You already submitted feedback. Thanks!")

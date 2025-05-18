import streamlit as st
from agent_registry import AGENTS
from utils.agent_runner import run_agent_safely
from memory.memory_utils import retrieve_similar_prompts

# 🧠 App settings
st.set_page_config(page_title="OmniAgent AI", layout="wide")
st.title("🤖 OmniAgent AI — Multi-Agent Reasoning Assistant")
st.caption("Interact with specialized agents powered by DeepSeek + Memory")

# 🚀 Agent selection
selected_agent_key = st.selectbox("🧠 Choose an Agent", options=list(AGENTS.keys()))
agent = AGENTS[selected_agent_key]

# 🧾 Description & context
st.markdown(f"**📝 Description**: {agent.description}")
st.markdown(f"**🔧 Tools**: {', '.join(agent.tools) or 'None'}")
st.markdown(f"**💾 Memory Scope**: `{agent.memory_scope}`")
st.markdown("---")

# 📥 Input area
user_input = None
if agent.input_type == "code":
    user_input = st.text_area("💻 Enter your code or question:")
elif agent.input_type == "file":
    uploaded_file = st.file_uploader("📁 Upload a file")
    if uploaded_file:
        user_input = uploaded_file.read().decode("utf-8")
else:
    user_input = st.text_input("🧠 Describe your task:")

# 🔁 Show related memory if any
if user_input:
    memory = retrieve_similar_prompts(user_input)
    if memory:
        with st.expander("🔁 Related Memory Found", expanded=False):
            for i, m in enumerate(memory[:3]):
                st.markdown(f"**#{i+1}**\n```\n{m.strip()}\n```")

# ▶️ Run agent
if st.button(f"Run {agent.name}"):
    if not user_input:
        st.warning("Please provide a task or file to process.")
    else:
        with st.spinner("Running agent..."):
            try:
                result = run_agent_safely(agent.name, user_input)
                st.success("✅ Agent completed the task")
                st.code(result, language="python" if agent.input_type == "code" else "text")
            except Exception as e:
                st.error(f"❌ Error while running agent: {e}")

        # 👍 Collect feedback
        if agent.learnable:
            st.markdown("### 🧠 Was this helpful?")
            feedback = st.radio("Feedback:", ["👍 Yes", "👎 No"], horizontal=True)
            if feedback:
                agent.learn(feedback, user_input, result)
                st.success("📝 Feedback recorded. Thank you!")

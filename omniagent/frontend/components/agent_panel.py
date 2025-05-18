import streamlit as st
from memory.memory_utils import retrieve_similar_prompts
from utils.agent_runner import run_agent_safely
from frontend.components.feedback_form import render_feedback_section

def render_agent_panel(agent):
    """
    Renders a full input/output panel for a given agent.
    Includes input box, memory display, result, and feedback.
    """
    st.header(f"🧠 {agent.name}")
    st.caption(agent.description)

    user_input = None
    result = None

    if agent.input_type == "code":
        user_input = st.text_area("💻 Code task or question")
    elif agent.input_type == "file":
        uploaded = st.file_uploader("📄 Upload file")
        if uploaded:
            user_input = uploaded.read().decode("utf-8")
    else:
        user_input = st.text_input("🧠 Task description")

    # 🔁 Memory Preview
    if user_input:
        memory = retrieve_similar_prompts(user_input)
        if memory:
            with st.expander("🔁 Relevant Memory", expanded=False):
                for i, m in enumerate(memory[:3]):
                    st.markdown(f"**#{i+1}**\n```\n{m.strip()}\n```")

    # ▶️ Run Agent
    if st.button(f"Run {agent.name}", key=f"run_{agent.name}"):
        if not user_input:
            st.warning("Please enter input.")
        else:
            with st.spinner("Thinking..."):
                result = run_agent_safely(agent.name, user_input)
                st.success("✅ Task complete")
                st.code(result, language="python" if agent.input_type == "code" else "text")

            # 👍 Feedback
            if agent.learnable:
                render_feedback_section(agent.name, user_input, result)

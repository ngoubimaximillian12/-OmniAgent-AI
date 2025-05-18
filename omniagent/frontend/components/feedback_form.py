import streamlit as st
from learning.feedback_loop import log_feedback

def render_feedback_section(agent_name: str, prompt: str, output: str):
    """
    Renders a feedback section with thumbs up/down options
    and sends data to the feedback logger.
    """
    st.markdown("### 🧠 Was this output helpful?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Yes", key=f"{agent_name}_yes"):
            log_feedback(agent=agent_name, prompt=prompt, output=output, feedback="Yes")
            st.success("✅ Thanks for your feedback!")

    with col2:
        if st.button("👎 No", key=f"{agent_name}_no"):
            log_feedback(agent=agent_name, prompt=prompt, output=output, feedback="No")
            st.warning("📝 We'll use this to improve!")

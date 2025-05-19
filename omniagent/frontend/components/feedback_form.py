import streamlit as st
from learning.feedback_loop import log_feedback

def render_feedback_section(agent_name: str, prompt: str, output: str):
    """
    Renders a feedback section with thumbs up/down buttons.
    Logs feedback to the learning feedback loop.
    """

    st.markdown("### 🧠 Was this output helpful?")

    col1, col2 = st.columns(2)

    # Use session state keys to disable buttons after feedback to prevent multiple clicks
    yes_key = f"{agent_name}_yes"
    no_key = f"{agent_name}_no"

    if yes_key not in st.session_state:
        st.session_state[yes_key] = False
    if no_key not in st.session_state:
        st.session_state[no_key] = False

    with col1:
        if st.button("👍 Yes", key=yes_key, disabled=st.session_state[yes_key] or st.session_state[no_key]):
            log_feedback(agent=agent_name, prompt=prompt, output=output, feedback="Yes")
            st.session_state[yes_key] = True
            st.success("✅ Thanks for your feedback!")

    with col2:
        if st.button("👎 No", key=no_key, disabled=st.session_state[yes_key] or st.session_state[no_key]):
            log_feedback(agent=agent_name, prompt=prompt, output=output, feedback="No")
            st.session_state[no_key] = True
            st.warning("📝 We'll use this to improve!")

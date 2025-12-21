import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="Body Fat & Body Composition Analyzer",
        page_icon="🧬",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def render_title():
    st.title("🧬 Body Fat & Body Composition Analyzer")
    st.caption(
        "AI-powered body fat estimation with fitness-focused insights "
        "based on standardized anthropometric measurements."
    )
    st.markdown("---")

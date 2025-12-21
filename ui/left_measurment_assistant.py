import streamlit as st

def render_measurement_assistant():
    st.markdown("## 🧍 Measurement Assistant")
    st.caption("Follow standardized steps to ensure accurate predictions")

    st.markdown("---")

    # ▶️ Measurement Video
    with st.expander("🎥 Watch: How to Take Body Measurements"):
        st.video(
            "https://youtu.be/O_080QAxU1A?si=S3-Xk2yF9FApdWJ1"
        )
        st.caption("Demonstration of standard anthropometric measurements")

    # 📐 Measurement Guidelines
    with st.expander("📐 Measurement Guidelines"):
        st.markdown("""
        **Before Measuring**
        - Use a flexible measuring tape
        - Measure on bare skin
        - Stand upright and relaxed

        **During Measurement**
        - Tape should be snug, not tight
        - Do not hold breath
        - Keep tape parallel to the ground

        **Best Practice**
        - Take **2–3 readings**
        - Use the **average value**
        """)

    # 🧠 Why Accuracy Matters
    with st.expander("🧠 Why Accurate Measurements Matter"):
        st.markdown("""
        Small measurement errors can significantly affect:
        - Body fat estimation
        - Lean mass calculation
        - Muscle quality metrics

        Accurate inputs ensure **reliable and meaningful results**.
        """)

    st.markdown("---")

    # ℹ️ Footer Note
    st.info(
        "This assistant helps reduce input error and improves model reliability. "
        "It is intended for educational and fitness insights."
    )

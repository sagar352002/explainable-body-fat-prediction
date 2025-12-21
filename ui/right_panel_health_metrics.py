import streamlit as st


def render_health_metrics_guide():
    st.subheader("📊 Health Metrics Guide")

    # -------------------------------------------------
    # Body Fat Percentage
    # -------------------------------------------------
    with st.expander("🧍 Body Fat Percentage"):
        st.markdown("""
        **What it measures:**  
        The proportion of total body weight that comes from fat tissue.

        **Formula (conceptual):**  
        `Body Fat % = (Fat Mass ÷ Total Body Weight) × 100`

        **Healthy Ranges (Adults):**

        **Men**
        - **< 6%** → Essential fat  
        - **6 – 13%** → Athletic  
        - **14 – 20%** → Fitness / Healthy  
        - **21 – 24%** → Overfat  
        - **≥ 25%** → Obese  

        **Women**
        - **< 14%** → Essential fat  
        - **14 – 20%** → Athletic  
        - **21 – 30%** → Fitness / Healthy  
        - **31 – 35%** → Overfat  
        - **≥ 36%** → Obese  

        **Why it matters:**  
        Body fat percentage is a more accurate indicator of health than BMI because it directly reflects fat accumulation rather than total weight.
        
        **Note:**  
        Very low body fat levels can be unhealthy and may affect hormones, immunity, and overall performance.
        """)

    # -------------------------------------------------
    # BMI
    # -------------------------------------------------
    with st.expander("📏 BMI – Body Mass Index"):
        st.markdown("""
        **What it measures:**  
        Overall body weight relative to height.

        **Formula:**  
        `BMI = Weight (kg) ÷ Height² (m)`

        **Healthy Ranges:**
        - **< 18.5** → Underweight  
        - **18.5 – 24.9** → Normal  
        - **25 – 29.9** → Overweight  
        - **≥ 30** → Obese  

        **Why it matters:**  
        BMI gives a quick screening of weight-related health risk, but does not distinguish muscle from fat.
        """)

    # -------------------------------------------------
    # FFMI
    # -------------------------------------------------
    with st.expander("🏋️ FFMI – Fat-Free Mass Index"):
        st.markdown("""
        **What it measures:**  
        Muscle mass adjusted for height (fat excluded).

        **Formula:**  
        `FFMI = Lean Mass ÷ Height² (m)`

        **Reference Ranges:**
        - **< 18** → Low muscle mass  
        - **18 – 20** → Average  
        - **20 – 22** → Athletic  
        - **> 22** → Very muscular  

        **Why it matters:**  
        FFMI is superior to BMI for evaluating muscular development and fitness.
        """)

    # -------------------------------------------------
    # FMI
    # -------------------------------------------------
    with st.expander("⚖️ FMI – Fat Mass Index"):
        st.markdown("""
        **What it measures:**  
        Fat mass relative to height.

        **Formula:**  
        `FMI = Fat Mass ÷ Height² (m)`

        **Reference Ranges:**
        - **< 3** → Lean  
        - **3 – 6** → Healthy  
        - **> 6** → Excess fat mass  

        **Why it matters:**  
        FMI isolates fat contribution and avoids BMI’s muscle–fat confusion.
        """)

    # -------------------------------------------------
    # MFR & MQI
    # -------------------------------------------------
    with st.expander("💪 Muscle Quality Metrics (MFR & MQI)"):
        st.markdown("""
        **MFR – Muscle-to-Fat Ratio**  
        **Formula:**  
        `MFR = Lean Mass ÷ Fat Mass`

        **Interpretation:**
        - **> 3.0** → Excellent body composition  
        - **1.5 – 3.0** → Normal  
        - **< 1.5** → Fat dominant  

        ---
        **MQI – Muscle Quality Index**  
        **Formula:**  
        `MQI = Lean Mass ÷ Total Weight`

        **Interpretation:**
        - **> 0.75** → High muscle quality  
        - **0.65 – 0.75** → Moderate  
        - **< 0.65** → Low muscle proportion  

        **Why these matter:**  
        These metrics describe how efficiently body weight is composed of lean tissue rather than fat.
        """)

    # -------------------------------------------------
    # Lean & Fat Mass
    # -------------------------------------------------
    with st.expander("🧬 Lean Mass & Fat Mass"):
        st.markdown("""
        **Fat Mass:**  
        Total weight of fat tissue in the body.  
        `Fat Mass = (Body Fat % ÷ 100) × Weight`

        **Lean Mass:**  
        Everything except fat (muscle, bones, organs, water).  
        `Lean Mass = Weight − Fat Mass`

        **Why it matters:**  
        Health improvement focuses on increasing lean mass while controlling fat mass.
        """)

    st.caption("📚 References: WHO • ACSM • Sports & Clinical Physiology Literature")

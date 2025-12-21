import streamlit as st
import pandas as pd
import pickle
import numpy as np
import statsmodels.api as sm
from ui.page_setup import setup_page, render_title
from ui.right_panel_health_metrics import render_health_metrics_guide
from ui.left_measurment_assistant import render_measurement_assistant
from llm_model import generate_fitness_summary
from feature_importance import (
    load_model_artifact,
    compute_feature_importance,
    build_llm_input
)
from ui.metric_caption import (
    fat_mass_caption,
    lean_mass_caption,
    ffmi_caption,
    fmi_caption,
    mfr_caption,
    mqi_caption
)
from ml.feature_engineering import (
    calculate_bmi,
    build_feature_df,
    FEATURE_ORDER
)
################## page configuration #######################################################################
setup_page()
# 🔹 TITLE & HEADER
# render_title()
######################################################################################################

# 🔹 LOAD MODEL
# =========================================================
@st.cache_resource
def load_model():
    with open("bodyfat_model.pkl", "rb") as f:
        obj = pickle.load(f)

    if isinstance(obj, dict):
        for key in ("model", "ols_model", "best_model", "pipeline"):
            if key in obj:
                return obj[key]
        return obj
    return obj

model = load_model()

# 🔹 Prediction
# =========================================================

@st.cache_data
def predict_bodyfat(user_input):
    X = build_feature_df(user_input)
    X = sm.add_constant(X, has_constant="add")
    return float(model.predict(X).values[0])

def body_composition(weight, height_cm, bf):
    h = height_cm * 0.01
    fat = (bf * 0.01) * weight
    lean = weight - fat
    inv_h2 = 1.0 / (h * h)

    return {
        "fat": fat,
        "lean": lean,
        "ffmi": lean * inv_h2,
        "fmi": fat * inv_h2,
        "mfr": lean / fat if fat != 0 else np.inf,
        "mqi": lean / weight
    }

# ################## Left Panel of ui #######################################################################
with st.sidebar:
    render_measurement_assistant()

# ######################################################################################################

center, right = st.columns([3, 1.4])

# ===================== CENTER PANEL ============================================================================
with center:
    st.title("💪 AI-Powered Body Fat Prediction and Composition Analysis")
    st.write("Clinical-grade prediction with explainable ML insights")

    with st.form("bf_form"):
        c1, c2 = st.columns(2)

        Age = c1.number_input("Age (years)", 18, 80, 28)
        Height = c1.number_input("Height (cm)", 140, 210, 175)
        Weight = c1.number_input("Weight (kg)", 40.0, 200.0, 72.0)
        Neck = c1.number_input("Neck (cm)", 20.0, 60.0, 37.0)
        Forearm = c1.number_input("Forearm (cm)", 20.0, 60.0, 29.0)
        Wrist = c1.number_input("Wrist (cm)", 10.0, 30.0, 17.0)
        Knee = c1.number_input("Knee (cm)", 25.0, 70.0, 40.0)

        Abdomen = c2.number_input("Abdomen (cm)", 50.0, 150.0, 91.0)
        Hip = c2.number_input("Hip (cm)", 60.0, 150.0, 98.0)
        Thigh = c2.number_input("Thigh (cm)", 30.0, 90.0, 57.0)
        Biceps = c2.number_input("Biceps (cm)", 20.0, 60.0, 32.0)

        submit = st.form_submit_button("Predict & Analyze 🔍")

    # ====================== COMPUTE ONCE ======================
    if submit:
        ui = {
            "Age": Age, "Neck": Neck, "Knee": Knee,
            "Forearm": Forearm, "Wrist": Wrist,
            "Abdomen": Abdomen, "Hip": Hip,
            "Thigh": Thigh, "Biceps": Biceps,
            "Weight": Weight, "Height": Height
        }

        bf = predict_bodyfat(ui)
        bmi = calculate_bmi(Weight, Height)
        comp = body_composition(Weight, Height, bf)

        feature_importance_df = compute_feature_importance(
            model=model,
            feature_order=FEATURE_ORDER,
            top_n=4
        )

        llm_input = build_llm_input(
            body_fat_percent=bf,
            bmi=bmi,
            lean_mass=comp["lean"],
            fat_mass=comp["fat"],
            ffmi=comp["ffmi"],
            fmi=comp["fmi"],
            mfr=comp["mfr"],
            mqi=comp["mqi"],
            feature_importance_df=feature_importance_df
        )

        insights = generate_fitness_summary(llm_input)

        # store results to avoid recompute on rerun
        st.session_state["results"] = (bf, bmi, comp, insights)
    def bodyfat_color(bf):
        if bf < 15:
            return "#16A34A"   # 🟢 Green (Lean / Athletic)
        elif bf < 22:
            return "#F59E0B"   # 🟡 Amber (Healthy)
        else:
            return "#DC2626"   # 🔴 Red (High)
    
        
    # ====================== RENDER ONLY ======================
    if "results" in st.session_state:
        bf, bmi, comp, insights = st.session_state["results"]

        bg_color = bodyfat_color(bf)

        st.markdown(
            f"""
            <div style="
                background:{bg_color};
                padding:20px;
                border-radius:14px;
                text-align:center;
                margin-bottom:12px;
            ">
                <div style="font-size:16px; color:#ECFDF5;">
                    🔥 BODY FAT
                </div>
                <div style="font-size:46px; font-weight:700; color:white;">
                    {bf:.2f}%
                </div>
                <div style="font-size:15px; color:#DCFCE7;">
                    BMI: {bmi:.2f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(float(min(bf / 50, 1.0)))

# ===================== BODY COMPOSITION METRICS =====================
        st.markdown("### 🧬 Body Composition")

        c1, c2, c3 = st.columns(3)

        c1.metric("🧬 Fat Mass (kg)", f"{comp['fat']:.2f}")
        c1.caption(fat_mass_caption(comp["fat"]))

        c2.metric("🧬 Lean Mass (kg)", f"{comp['lean']:.2f}")
        c2.caption(lean_mass_caption(comp["lean"]))

        c3.metric("💪 MFR", f"{comp['mfr']:.2f}")
        c3.caption(mfr_caption(comp["mfr"]))


        # ===================== MUSCLE & QUALITY METRICS =====================
        st.markdown("### 💪 Muscle & Quality Metrics")

        c4, c5, c6 = st.columns(3)

        c4.metric("💪 FFMI", f"{comp['ffmi']:.2f}")
        c4.caption(ffmi_caption(comp["ffmi"]))

        c5.metric("⚖ FMI", f"{comp['fmi']:.2f}")
        c5.caption(fmi_caption(comp["fmi"]))

        c6.metric("🔬 MQI", f"{comp['mqi']:.2f}")
        c6.caption(mqi_caption(comp["mqi"]))


        # ===================== LLM FITNESS INSIGHTS =====================
        st.markdown("### 🤖Fitness Insights")

        for i, point in enumerate(insights):
            if i < 3:
                # Key summary lines (highlighted)
                st.markdown(f"**{point}**")
            else:
                # Supporting insights
                st.markdown(f"- {point}")

# ===========================================================================================================================




######################################################################################################
################## Right Panel #######################################################################
with right:
    render_health_metrics_guide()

######################################################################################################


import streamlit as st

def render_center_panel(
    model,
    FEATURE_ORDER,
    predict_bodyfat,
    calculate_bmi,
    body_composition,
    compute_feature_importance,
    build_llm_input,
    generate_fitness_summary
):
    st.title("💪 Body Fat & Body Composition Analyzer")
    st.write("ML-powered prediction with clinical-grade interpretation.")

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

    if submit:
        ui = {
            "Age": Age, "Neck": Neck, "Knee": Knee,
            "Forearm": Forearm, "Wrist": Wrist,
            "Abdomen": Abdomen, "Hip": Hip,
            "Thigh": Thigh, "Biceps": Biceps,
            "Weight": Weight, "Height": Height
        }

        # 🔹 ML prediction
        bf = predict_bodyfat(ui)
        bmi = calculate_bmi(Weight, Height)
        comp = body_composition(Weight, Height, bf)

        st.success(f"🔥 Body Fat: **{bf:.2f}%** | BMI: **{bmi:.2f}**")
        st.progress(min(bf / 50, 1.0))

        m1, m2, m3 = st.columns(3)
        m1.metric("Fat Mass (kg)", f"{comp['fat']:.2f}")
        m2.metric("Lean Mass (kg)", f"{comp['lean']:.2f}")
        m3.metric("MFR", f"{comp['mfr']:.2f}")

        m4, m5, m6 = st.columns(3)
        m4.metric("FFMI", f"{comp['ffmi']:.2f}")
        m5.metric("FMI", f"{comp['fmi']:.2f}")
        m6.metric("MQI", f"{comp['mqi']:.2f}")

        # =========================================================
        # 🔹 FEATURE IMPORTANCE + LLM
        # =========================================================
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

        with st.spinner("🤖 Generating fitness insights..."):
            insights = generate_fitness_summary(llm_input)

        st.subheader("🏋️ AI-Generated Fitness Summary")
        for i, point in enumerate(insights):
            if i < 3:
                st.write(point)
            else:
                st.write("•", point)

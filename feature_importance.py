import pickle
import pandas as pd


# =========================================================
# 🔹 LOAD MODEL (ROBUST)
# =========================================================
def load_model_artifact(path="bodyfat_model.pkl"):
    """
    Supports both:
    1) Pickle containing ONLY statsmodels RegressionResultsWrapper
    2) Pickle containing dict with model + metadata
    """
    with open(path, "rb") as f:
        artifact = pickle.load(f)

    if isinstance(artifact, dict):
        model = artifact.get("model", artifact)
        feature_order = artifact.get("feature_order", None)
    else:
        model = artifact
        feature_order = None

    return model, feature_order


# =========================================================
# 🔹 FEATURE IMPORTANCE (MLR COEFFICIENTS → %)
# =========================================================
# @st.cache_data(show_spinner=False)
def compute_feature_importance(model, feature_order, top_n=4):
    """
    Uses normalized absolute MLR coefficients as feature importance (%).
    """
    coef = model.params.drop("const")
    abs_coef = coef.abs()

    total_importance = abs_coef.sum()

    df = pd.DataFrame({
        "feature": feature_order,
        "coefficient": coef.values,
        "importance_percent": (abs_coef.values / total_importance) * 100
    })

    df = df.sort_values("importance_percent", ascending=False)
    return df.head(top_n)


# =========================================================
# 🔹 BUILD DATA THAT WILL GO TO LLM
# =========================================================
def build_llm_input(
    *,
    body_fat_percent,
    bmi,
    lean_mass,
    fat_mass,
    ffmi,
    fmi,
    mfr,
    mqi,
    feature_importance_df
):
    """
    ONLY prepares structured data.
    No prompt. No LLM logic.
    """

    return {
        "predictions": {
            "body_fat_percent": round(body_fat_percent, 2),
            "bmi": round(bmi, 2)
        },
        "body_composition": {
            "lean_mass_kg": round(lean_mass, 2),
            "fat_mass_kg": round(fat_mass, 2),
            "ffmi": round(ffmi, 2),
            "fmi": round(fmi, 2),
            "muscle_to_fat_ratio": round(mfr, 2),
            "muscle_quality_index": round(mqi, 2)
        },
        "feature_importance": [
            {
                "feature_name": row.feature,
                "coefficient": round(row.coefficient, 4),
                "importance_percent": round(row.importance_percent, 2)
            }
            for _, row in feature_importance_df.iterrows()
        ],
        "explainability_method": "MLR_coefficients_percentage"
    }




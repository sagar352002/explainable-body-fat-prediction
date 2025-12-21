import pandas as pd

# =========================================================
# 🔹 CONSTANTS
# =========================================================
LAMBDA_DICT = {
    "Abdomen": -0.0601,
    "Hip": -1.2909,
    "Thigh": -1.5335,
    "Biceps": -3.5362,
    "Bmi": -0.4095
}

FEATURE_ORDER = [
    "Age", "Neck", "Knee", "Forearm", "Wrist",
    "Abdomen_BT", "Hip_BT", "Thigh_BT", "Biceps_BT", "Bmi_BT"
]

# =========================================================
# 🔹 FUNCTIONS (LOGIC UNCHANGED)
# =========================================================
def calculate_bmi(weight, height_cm):
    h = height_cm * 0.01
    return weight / (h * h)


def transform_features(user_input: dict) -> dict:
    out = {}
    for col, val in user_input.items():
        if col in LAMBDA_DICT:
            out[f"{col}_BT"] = max(val, 0.01) ** LAMBDA_DICT[col]
        else:
            out[col] = val
    return out


def build_feature_df(user_input: dict) -> pd.DataFrame:
    data = user_input.copy()  # no mutation
    data["Bmi"] = calculate_bmi(data["Weight"], data["Height"])
    X = pd.DataFrame([transform_features(data)])
    return X.reindex(columns=FEATURE_ORDER)

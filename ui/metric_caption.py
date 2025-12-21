def fat_mass_caption(fat):
    if fat < 12:
        return "🟢 Lean"
    elif fat < 20:
        return "🟡 Controlled"
    else:
        return "🔴 High"

def lean_mass_caption(lean):
    if lean > 55:
        return "💪 Strong"
    elif lean > 45:
        return "🟡 Average"
    else:
        return "🔴 Low"

def ffmi_caption(ffmi):
    if ffmi >= 20:
        return "🏋️ Athletic"
    elif ffmi >= 18:
        return "💪 Fit"
    else:
        return "⚠️ Needs Improvement"

def fmi_caption(fmi):
    if fmi < 3:
        return "🟢 Lean"
    elif fmi < 6:
        return "🟡 Healthy"
    else:
        return "🔴 High Fat"

def mfr_caption(mfr):
    if mfr >= 3:
        return "🔥 Excellent"
    elif mfr >= 1.5:
        return "🟡 Normal"
    else:
        return "🔴 Fat Dominant"

def mqi_caption(mqi):
    if mqi >= 0.75:
        return "⭐ High Quality"
    elif mqi >= 0.65:
        return "🟡 Moderate"
    else:
        return "🔴 Low Quality"
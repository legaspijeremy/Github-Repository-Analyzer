def calculate_complexity_score(
    documentation_score,
    total_files,
    total_python_files,
    contributors
):
    score = 0

    # ----------------------------
    # Documentation (10 points)
    # ----------------------------

    score += min(documentation_score / 10, 10)

    # ----------------------------
    # Total Files (40 points)
    # ----------------------------

    if total_files >= 300:
        score += 40
    elif total_files >= 150:
        score += 30
    elif total_files >= 50:
        score += 20
    else:
        score += 10

    # ----------------------------
    # Python Files (30 points)
    # ----------------------------

    if total_python_files >= 100:
        score += 30
    elif total_python_files >= 50:
        score += 25
    elif total_python_files >= 20:
        score += 20
    elif total_python_files >= 10:
        score += 15
    else:
        score += 10

    # ----------------------------
    # Contributors (20 points)
    # ----------------------------

    if contributors >= 100:
        score += 20
    elif contributors >= 20:
        score += 15
    elif contributors >= 5:
        score += 10
    else:
        score += 5

    return round(score)


def classify_project(score):

    if score >= 85:
        return "Very Complex"

    elif score >= 65:
        return "Complex"

    elif score >= 35:
        return "Medium"

    return "Simple"
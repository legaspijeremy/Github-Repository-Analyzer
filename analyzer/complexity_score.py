def calculate_complexity_score(
    documentation_score,
    python_files,
    total_loc,
    avg_complexity,
    maintainability
):
    
    score = 0

    # Documentation (20 points)
    score += min(documentation_score, 100) * 0.20

    # Repository Scale (30 points)

    if python_files >= 100:
        score += 15
    elif python_files >= 50:
        score += 10
    elif python_files >= 20:
        score += 5

    if total_loc >= 20000:
        score += 15
    elif total_loc >= 10000:
        score += 10
    elif total_loc >= 5000:
        score += 5

    # Complexity (20 points)

    if avg_complexity <= 3:
        score += 20
    elif avg_complexity <= 6:
        score += 15
    elif avg_complexity <= 10:
        score += 10
    else:
        score += 5

    # Maintainability (30 points)

    score += min(maintainability, 100) * 0.30

    return round(score)

def classify_project(score):

    if score >= 90:
        return "Very Complex"

    elif score >= 70:
        return "Complex"

    elif score >= 35:
        return "Medium"

    return "Simple"
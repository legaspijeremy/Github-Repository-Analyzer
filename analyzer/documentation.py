import re


def score_documentation(readme: str):
    score = 0

    text = readme.lower()

    checks = {
    "installation": "install" in text,
    "usage": "usage" in text,
    "examples": "example" in text,
    "api_docs": "api" in text,
    "contributing": "contributing" in text,
    "license": "license" in text,
    "getting_started": "getting started" in text,
    "faq": "faq" in text,
    "roadmap": "roadmap" in text,
    }

    # README length
    if len(readme) > 500:
        score += 10

    if len(readme) > 2000:
        score += 10

    # Headings
    headings = len(
        re.findall(r"^#{1,6}\s", readme, re.MULTILINE)
    )

    if headings >= 3:
        score += 10

    if headings >= 6:
        score += 10

    # Code blocks
    code_blocks = readme.count("```")

    if code_blocks >= 2:
        score += 10

    if code_blocks >= 6:
        score += 10

    # Section checks
    for passed in checks.values():
        if passed:
            score += 5

    metrics = {
        "readme_length": len(readme),
        "headings": headings,
        "code_blocks": code_blocks
    }

    return min(score, 100), checks, metrics
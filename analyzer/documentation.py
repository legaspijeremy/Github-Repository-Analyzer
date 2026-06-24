import re


def score_documentation(readme: str):
    score = 0

    # Basic metrics first
    headings = len(
        re.findall(r"^#{1,6}\s", readme, re.MULTILINE)
    )

    code_blocks = readme.count("```")

    markdown_links = len(
        re.findall(r"\[.*?\]\(.*?\)", readme)
    )

    reference_links = len(
        re.findall(r"\[.*?\]", readme)
    )
    links = max(markdown_links, reference_links)

    markdown_images = len(
        re.findall(r"!\[.*?\]\(.*?\)", readme)
    )

    html_images = len(
        re.findall(r"<img\s+[^>]*src=", readme, re.IGNORECASE)
    )
    images = markdown_images + html_images

    tables = readme.count("|")

    # Universal checks
    checks = {
        "sufficient_length": len(readme) > 1000,
        "structured_sections": headings >= 4,
        "contains_examples": code_blocks >= 2,
        "contains_links": links >= 3,
        "contains_images": images >= 1,
    }

    # README length
    if len(readme) > 500:
        score += 10

    if len(readme) > 1500:
        score += 10

    # Structure
    if headings >= 3:
        score += 15

    if headings >= 6:
        score += 10

    # Examples
    if code_blocks >= 2:
        score += 15

    if code_blocks >= 6:
        score += 10

    # Links
    if links >= 3:
        score += 10

    if links >= 10:
        score += 10

    # Images
    if images >= 1:
        score += 5

    # Tables
    if tables >= 10:
        score += 5

    # Bonus checks
    for passed in checks.values():
        if passed:
            score += 2

    metrics = {
        "readme_length": len(readme),
        "headings": headings,
        "code_blocks": code_blocks,
        "links": links,
        "images": images,
        "tables": tables,
        "sections_found": sum(checks.values()),
    }

    return min(score, 100), checks, metrics
import time

start_time = time.time()

from analyzer.github_client import (
    get_repo,
    get_readme
)

from analyzer.documentation import (
    score_documentation
)

from analyzer.repo_metrics import (
    get_repository_metrics,
    get_file_tree
)

from analyzer.code_quality import analyze_code_quality

from analyzer.complexity_score import (
    calculate_complexity_score,
    classify_project
)

from analyzer.ai_summary import generate_ai_summary

url = input("Repository URL: ")

# ----------------------------
# Fetch Repository
# ----------------------------

start = time.time()
repo = get_repo(url)
print(f"[TIME] Fetch Repository: {time.time() - start:.2f}s")

# ----------------------------
# Repository Metrics
# ----------------------------

start = time.time()

print("Fetching repository metrics...")
repo_metrics = get_repository_metrics(repo)

print(f"[TIME] Repository Metrics: {time.time() - start:.2f}s")

# ----------------------------
# File Tree
# ----------------------------

start = time.time()

print("Fetching file tree...")
files = get_file_tree(repo)

print(f"[TIME] File Tree: {time.time() - start:.2f}s")

# ----------------------------
# README
# ----------------------------

start = time.time()

print("Fetching README...")
readme = get_readme(repo)

print(f"[TIME] README: {time.time() - start:.2f}s")

# ----------------------------
# Documentation Analysis
# ----------------------------

start = time.time()

print("Analyzing documentation...")
score, checks, metrics = score_documentation(readme)

print(f"[TIME] Documentation Analysis: {time.time() - start:.2f}s")

# ----------------------------
# Repository Information
# ----------------------------

print("\nRepository Information")
print("-" * 30)

print("Name:", repo.name)
print("Description:", repo.description)
print("Stars:", repo.stargazers_count)

# ----------------------------
# Repository Metrics
# ----------------------------

print("\nRepository Metrics")
print("-" * 30)

for key, value in repo_metrics.items():
    print(f"{key}: {value}")

# ----------------------------
# Documentation Score
# ----------------------------

print(f"\nDocumentation Quality Score: {score}/100")

# ----------------------------
# Documentation Analysis
# ----------------------------

print("\nDocumentation Analysis")
print("-" * 30)

for item, passed in checks.items():
    status = "✓" if passed else "✗"
    print(f"{status} {item}")

# ----------------------------
# Code Quality Analysis
# ----------------------------

start = time.time()

print("\nAnalyzing code quality...")
quality = analyze_code_quality(files, repo)

print(f"[TIME] Code Quality Analysis: {time.time() - start:.2f}s")

print("\nCode Quality Analysis")
print("-" * 30)
print(f"Python Files: {quality['python_files']}")
print(f"Lines of Code: {quality['total_loc']}")
print(f"Average Function Length: {quality['avg_function_length']}")
print(f"Average Class Size: {quality['avg_class_size']}")
print(f"Cyclomatic Complexity: {quality['avg_complexity']}")
print(f"Maintainability Index: {quality['avg_maintainability']}")

all_python_files = len(
    [f for f in files if f.endswith(".py")]
)

print(f"Production Python Files: {quality['python_files']}")
print(f"Total Python Files: {all_python_files}")

# ----------------------------
# Project Complexity
# ----------------------------

start = time.time()

total_files = len(files)

total_python_files = len(
    [
        file
        for file in files
        if file.endswith(".py")
    ]
)

complexity_score = calculate_complexity_score(
    documentation_score=score,
    total_files=total_files,
    total_python_files=total_python_files,
    contributors=repo_metrics["contributors"]
)

classification = classify_project(complexity_score)

print(f"[TIME] Complexity Score: {time.time() - start:.2f}s")

print("\nProject Complexity Score")
print("-" * 30)
print(f"Complexity Score: {complexity_score}/100")
print(f"Complexity Level: {classification}")

# ----------------------------
# Complexity Factors
# ----------------------------

print("\nComplexity Factors")
print("-" * 30)

print(f"Total Files         : {total_files}")
print(f"Total Python Files  : {total_python_files}")
print(f"Contributors        : {repo_metrics['contributors']}")
print(f"Documentation Score : {score}/100")

# ----------------------------
# Summary
# ----------------------------

if classification == "Very Complex":
    summary = (
        "Large-scale repository with a substantial codebase "
        "and broad project scope."
    )

elif classification == "Complex":
    summary = (
        "Well-developed repository with significant size "
        "and engineering effort."
    )

elif classification == "Medium":
    summary = (
        "Moderately sized repository suitable for "
        "medium-scale software projects."
    )

else:
    summary = (
        "Small repository with a focused codebase."
    )

print("\nSummary")
print("-" * 30)
print(summary)

# ----------------------------
# AI Project Summary
# ----------------------------

start = time.time()

print("\nGenerating AI Project Summary...")

ai_summary = generate_ai_summary(
    repo_name=repo.name,
    description=repo.description,
    readme=readme,
    repo_metrics=repo_metrics,
    documentation_score=score,
    documentation_metrics=metrics,
    code_quality=quality,
    complexity_score=complexity_score,
    total_files=total_files,
    total_python_files=total_python_files,
)

print(f"[TIME] AI Summary: {time.time() - start:.2f}s")

print("\nAI Project Summary")
print("-" * 30)
print(ai_summary)

# ----------------------------
# Documentation Metrics
# ----------------------------

print("\nDocumentation Metrics")
print("-" * 30)

for key, value in metrics.items():
    print(f"{key}: {value}")

# ----------------------------
# File Tree
# ----------------------------

print("\nFile Tree")
print("-" * 30)

print(f"Total Files: {len(files)}")

python_files = [
    f for f in files
    if f.endswith(".py")
]

print(f"Python Files: {len(python_files)}")

print("\nSample Files:")

for file in files[:10]:
    print(file)

# ----------------------------
# README Preview
# ----------------------------

print("\nREADME Preview")
print("-" * 30)

print(readme[:300])

# ----------------------------
# Total Time
# ----------------------------

elapsed = time.time() - start_time

print("\nAnalysis Complete")
print("-" * 30)
print(f"Completed in {elapsed:.2f} seconds")

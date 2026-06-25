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

url = input("Repository URL: ")

# Fetch repository
repo = get_repo(url)

# Repository metrics
print("Fetching repository metrics...")
repo_metrics = get_repository_metrics(repo)

# File tree
print("Fetching file tree...")
files = get_file_tree(repo)

# README
print("Fetching README...")
readme = get_readme(repo)

print("Analyzing documentation...")
# Documentation analysis
score, checks, metrics = score_documentation(readme)

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
# Code Quality Metrics
# ----------------------------
print("\nAnalyzing code quality...")
quality = analyze_code_quality(repo)

print("\nCode Quality Analysis")
print("-" * 30)
print(f"Python Files: {quality['python_files']}")
print(f"Lines of Code: {quality['total_loc']}")
print(f"Average Function Length: {quality['avg_function_length']}")
print(f"Average Class Size: {quality['avg_class_size']}")
print(f"Cyclomatic Complexity: {quality['avg_complexity']}")
print(f"Maintainability Index: {quality['avg_maintainability']}")

# ----------------------------
# Complexity Score
# ----------------------------
complexity_score = calculate_complexity_score(
    documentation_score=score,
    python_files=quality["python_files"],
    total_loc=quality["total_loc"],
    avg_complexity=quality["avg_complexity"],
    maintainability=quality["avg_maintainability"]
)

classification = classify_project(
    complexity_score
)

print("\nProject Complexity")
print("-" * 30)
print(f"Complexity Score: {complexity_score}/100")
print(f"Complexity Level: {classification}")

#Complexity Factors

print("\nComplexity Factors")
print("-" * 30)

print(f"Python Files : {quality['python_files']}")
print(f"Lines of Code: {quality['total_loc']}")
print(f"Contributors : {repo_metrics['contributors']}")

if classification == "Very Complex":
    summary = "Large-scale repository with extensive implementation."

elif classification == "Complex":
    summary = "Well-developed project with significant implementation."

elif classification == "Medium":
    summary = "Moderately sized project with balanced complexity."

else:
    summary = "Small repository with limited implementation."

print("\nSummary")
print("-" * 30)
print(summary)

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

elapsed = time.time() - start_time

print("\nAnalysis Complete")
print("-" * 30)
print(f"Completed in {elapsed:.2f} seconds")
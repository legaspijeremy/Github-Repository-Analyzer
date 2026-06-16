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

print(f"\nDocumentation Score: {score}/100")

# ----------------------------
# Documentation Analysis
# ----------------------------

print("\nDocumentation Analysis")
print("-" * 30)

for item, passed in checks.items():
    status = "✓" if passed else "✗"
    print(f"{status} {item}")

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
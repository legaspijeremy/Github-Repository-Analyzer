SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build"
}


def get_repository_metrics(repo):

    return {
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "language": repo.language,
        "contributors": repo.get_contributors().totalCount,
        "commit_count": repo.get_commits().totalCount,
        "open_issues": repo.open_issues_count,
    }

def get_file_tree(repo):
    """
    Retrieve the complete repository file tree
    using GitHub's Git Tree API.
    """

    print("Fetching repository tree...")

    files = []

    try:

        tree = repo.get_git_tree(
            repo.default_branch,
            recursive=True
        )

        for item in tree.tree:

            # Ignore directories
            if item.type != "blob":
                continue

            # Skip ignored folders
            parts = item.path.split("/")

            if any(
                part in SKIP_DIRS
                for part in parts
            ):
                continue

            files.append(item.path)

    except Exception as e:
        print(f"Error fetching repository tree: {e}")

    return files
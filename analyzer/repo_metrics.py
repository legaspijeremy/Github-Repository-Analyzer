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


def get_file_tree(repo, path=""):

    files = []

    print(f"Scanning: {path or '/'}")

    try:
        contents = repo.get_contents(path)

        for item in contents:

            if item.type == "file":
                files.append(item.path)

            elif item.type == "dir":

                if item.name in SKIP_DIRS:
                    continue

                files.extend(
                    get_file_tree(
                        repo,
                        item.path
                    )
                )

    except Exception as e:
        print(f"Error scanning {path}: {e}")

    return files
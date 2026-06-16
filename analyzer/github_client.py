from github import Github
from dotenv import load_dotenv
import os
import base64

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

github = Github(token)


def get_repo(repo_url: str):
    repo_name = "/".join(
        repo_url.rstrip("/").split("/")[-2:]
    )

    return github.get_repo(repo_name)


def get_readme(repo):
    readme = repo.get_readme()

    content = base64.b64decode(
        readme.content
    ).decode("utf-8")

    return content
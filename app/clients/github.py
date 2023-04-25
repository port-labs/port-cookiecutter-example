from github import Github

from core.config import settings


g = Github(settings.GH_ACCESS_TOKEN, timeout=60)


def create_repo(github_org: str, github_repo: str):
    user = g.get_user()
    org = user if user.login == github_org else g.get_organization(github_org)
    org.create_repo(github_repo, private=True)

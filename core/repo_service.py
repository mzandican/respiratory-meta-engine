from github import Github
import os

class RepoService:
    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")
        org_name = os.getenv("GITHUB_ORG")

        self.client = Github(token)
        self.org = self.client.get_organization(org_name)

    def get_all_repos(self):
        return list(self.org.get_repos())

    def create_repo(self, name, private=True):
        return self.org.create_repo(name=name, private=private)

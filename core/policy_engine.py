from pydantic import BaseModel

class PolicyResult(BaseModel):
    repo_name: str
    compliant: bool
    issues: list[str]

class PolicyEngine:
    def evaluate(self, repo):
        issues = []

        contents = [c.path for c in repo.get_contents("")]

        if "README.md" not in contents:
            issues.append("Missing README")

        if ".github/workflows" not in contents:
            issues.append("Missing CI/CD")

        return PolicyResult(
            repo_name=repo.name,
            compliant=len(issues) == 0,
            issues=issues
      )

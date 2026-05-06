import os
from dotenv import load_dotenv
from rich import print
from repo_service import RepoService
from policy_engine import PolicyEngine
from sync_engine import SyncEngine

load_dotenv()

class RespiratoryEngine:
    def __init__(self):
        self.dry_run = os.getenv("DRY_RUN", "true").lower() == "true"
        self.repo_service = RepoService()
        self.policy_engine = PolicyEngine()
        self.sync_engine = SyncEngine(self.dry_run)

    def run(self):
        print("[bold cyan]🌬 Starting Respiratory Cycle[/bold cyan]")

        repos = self.repo_service.get_all_repos()

        for repo in repos:
            policy_result = self.policy_engine.evaluate(repo)

            if not policy_result.compliant:
                print(f"[yellow]⚠ Repo non-compliant: {repo.name}[/yellow]")
                self.sync_engine.remediate(repo, policy_result)

        print("[green]✅ Cycle complete[/green]")

if __name__ == "__main__":
    RespiratoryEngine().run()

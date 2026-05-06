from rich import print

class SyncEngine:
    def __init__(self, dry_run=True):
        self.dry_run = dry_run

    def remediate(self, repo, policy_result):
        print(f"[blue]🔧 Fixing {repo.name}[/blue]")

        for issue in policy_result.issues:
            print(f" - {issue}")

        if self.dry_run:
            print("[grey]DRY RUN: No changes applied[/grey]")
            return

        # Example fix: create README
        if "Missing README" in policy_result.issues:
            repo.create_file(
                "README.md",
                "Add README",
                "# Auto-generated README"
            )

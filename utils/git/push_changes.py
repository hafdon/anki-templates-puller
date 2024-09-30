from git import GitCommandError


def push_changes(repo, remote_name="origin", branch="main"):
    try:
        origin = repo.remote(name=remote_name)
        origin.push(refspec=f"{branch}:{branch}")
        print(f"Pushed changes to remote '{remote_name}' on branch '{branch}'.")
    except GitCommandError as e:
        print(f"Git push failed: {e}")
    except Exception as e:
        print(f"Error during Git push: {e}")

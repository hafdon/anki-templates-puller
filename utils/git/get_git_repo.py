from git import GitCommandError, Repo


def get_git_repo(path):
    """
    Initialize and return a GitPython Repo object.
    """
    try:
        repo = Repo(path)
        if repo.bare:
            print("Git repository is bare.")
            return None
        return repo
    except GitCommandError as e:
        print(f"Git command error: {e}")
        return None
    except Exception as e:
        print(f"Error initializing Git repository: {e}")
        return None

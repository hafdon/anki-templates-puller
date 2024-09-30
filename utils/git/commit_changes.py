from fetch_templates import COMMIT_MESSAGE_TEMPLATE


from git import GitCommandError


from datetime import datetime


def commit_changes(repo):
    """
    Stage changes and commit them to the repository.
    """
    try:
        # Stage all changes in the templates directory
        repo.git.add(A=True)  # Stages all changes

        # Check if there is anything to commit
        if repo.is_dirty(untracked_files=True):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_message = COMMIT_MESSAGE_TEMPLATE.format(timestamp=timestamp)
            repo.index.commit(commit_message)
            print(f"Committed changes with message: '{commit_message}'")
        else:
            print("No changes to commit.")
    except GitCommandError as e:
        print(f"Git command error during commit: {e}")
    except Exception as e:
        print(f"Error during Git commit: {e}")

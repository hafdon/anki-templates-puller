from fetch_templates import (
    GIT_REPO_PATH,
    fetch_model_info,
    fetch_model_style_info,
    fetch_note_types,
    save_template,
    save_style,
)


import time

from utils.git.push_changes import push_changes
from utils.git.commit_changes import commit_changes
from utils.git.get_git_repo import get_git_repo


def main():
    # Initialize Git repository
    repo = get_git_repo(GIT_REPO_PATH)
    if not repo:
        print("Failed to initialize Git repository. Exiting.")
        return

    # Fetch all note types
    note_types = fetch_note_types()
    if not note_types:
        print("No note types found. Exiting.")
        return

    print(f"Found {len(note_types)} note types.")

    # Iterate over each note type and fetch its model info
    for model_name in note_types:
        model_info = fetch_model_info(model_name)
        style_info = fetch_model_style_info(model_name)
        if model_info:
            save_template(model_name, model_info)
            # To respect any rate limits or avoid overwhelming AnkiConnect
            time.sleep(0.2)  # Adjust as needed
        else:
            print(f"Failed to fetch info for model '{model_name}'.")

        if style_info:
            save_style(model_name, style_info)
            time.sleep(0.2)
        else:
            print(f"Failed to fetch style info for model `{model_name}")

    # Commit any changes to Git
    commit_changes(repo)

    # Push changes
    push_changes(repo)


if __name__ == "__main__":
    main()

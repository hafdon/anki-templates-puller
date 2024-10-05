import os
import json
import requests


# ------------------------------ Configuration ------------------------------

# AnkiConnect configuration
ANKI_CONNECT_URL = "http://localhost:8765"

# Directory to store card templates
TEMPLATES_DIR = "card_templates"

# Directory to store card styles
STYLES_DIR = "card_styles"

# Git repository path (current directory)
GIT_REPO_PATH = os.getcwd()

# Commit message template
COMMIT_MESSAGE_TEMPLATE = "Update Anki card templates: {timestamp}"

# -----------------------------------------------------------------------------


def invoke(action, params=None, version=6):
    """
    Helper function to communicate with AnkiConnect.
    """
    payload = {"action": action, "version": version}
    if params:
        payload["params"] = params

    try:
        response = requests.post(ANKI_CONNECT_URL, json=payload)
        response.raise_for_status()
        result = response.json()

        if result.get("error"):
            print(f"Error with action '{action}': {result['error']}")
            return None

        return result.get("result")
    except requests.exceptions.RequestException as e:
        print(f"AnkiConnect request failed: {e}")
        return None


def fetch_note_types():
    """
    Fetch all note types from Anki.
    """
    return invoke("modelNames")


def fetch_model_info(model_name):
    """
    Fetch detailed information about a specific note type (model).
    """
    return invoke("modelTemplates", {"modelName": model_name})


def fetch_model_style_info(model_name):
    """
    Fetch css information about a specific note type (model).
    """
    return invoke("modelStyling", {"modelName": model_name})


def save_template(model_name, model_info):
    """
    Save the card templates of a note type to a JSON file.
    """
    if not os.path.exists(TEMPLATES_DIR):
        os.makedirs(TEMPLATES_DIR)

    filename = f"{model_name}.json"
    filepath = os.path.join(TEMPLATES_DIR, filename)

    # Serialize model_info to JSON
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(model_info, f, ensure_ascii=False, indent=4)

    print(f"Saved template for model '{model_name}' to '{filepath}'.")


def save_style(model_name, model_info):
    """
    Save the card styling (css) of a note type to a JSON file.
    """
    if not os.path.exists(STYLES_DIR):
        os.makedirs(STYLES_DIR)

    filename = f"{model_name}.css"
    filepath = os.path.join(STYLES_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(model_info, f, ensure_ascii=False, indent=4)

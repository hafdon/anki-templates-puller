import os
from invoke import invoke


STYLE_FILE = "style.css"
UPDATE_DIR = "to_update"
UPDATE_MODEL_STYLING_COMMAND = "updateModelStyling"


def update_style(model_name):

    filepath = os.path.join(UPDATE_DIR, STYLE_FILE)

    # Read the contents of the CSS file
    try:
        with open(filepath, "r") as file:
            css_content = file.read()

        invoke(
            UPDATE_MODEL_STYLING_COMMAND,
            {"model": {"name": model_name, "css": css_content}},
        )

        print(f"Successfully updated {model_name} with styling from {filepath}.")

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example Usage
# model_name = "Basic_Noun_Clone"
# update_style(model_name)

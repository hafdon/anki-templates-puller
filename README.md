# Anki Templates Puller

A Python-based tool to fetch Anki card templates via AnkiConnect, store them as JSON files, and manage them using Git for version control.

## Features

- **Fetch Templates:** Retrieve all Anki note types and their card templates using AnkiConnect.
	- **JSON Storage:** Store each card template as a formatted JSON file in the `card_templates/` directory.
- **Fetch Styles:** Retrieve all Anki note styles (css) using AnkiConnect.
	- **JSON Storage:** Store each card style as a formatted JSON file in the `card_styles/` directory.
- **Git Integration:** Automatically commit changes to a Git repository for version control.
- **Testing:** Includes a test script to verify AnkiConnect interactions.

## Prerequisites

- **Anki:** Ensure Anki is installed and running on your machine.
- **AnkiConnect Add-on:** Install the [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on in Anki.
- **Python 3.7+**
- **Git:** Installed and initialized in your project directory.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hafdon/anki-templates-puller.git
   cd anki-templates-puller
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Ensure Anki and AnkiConnect Are Running:**

   - Open Anki to activate AnkiConnect.

2. **Run the Script:**

   ```bash
   python main.py
   ```
   
   - This will fetch all note types, retrieve their templates, save them as JSON files in `card_templates/`, and commit any changes to the Git repository.

## Testing

Run the test script to verify AnkiConnect's functionality:

```bash
python -m unittest discover -s test
```

## Formatting

Run the formatting script to see the card templates with proper indentation

```bash
python utils/render_json.py card_templates/Basic.json > temp.html
```

### Warning!

The template that is fetched includes both the front and back, so the re-renderer will generate an HTML page that has both these on it. If you are manually copying-and-pasting the formatted text into your Anki template, be sure to separate the "Front" and "Back" parts, and delete the "Front" and "Back" indicator text, or you'll end up with a messed up template!

## Git Workflow

- **Automatic Commits:** The script stages and commits any changes to the `card_templates/` directory with a timestamped message.
- **Viewing Changes:**
  ```bash
  git status
  git log --oneline
  ```
- **Pushing to Remote Repository (Optional):**
  ```bash
  git push origin main
  ```

## Update Model Styling Script

This script reads CSS styling from `style.css` located in the `to_update/` directory and applies it to a specified model using the `updateModelStyling` command.

### How it works:

1. **CSS file**: Reads the styling from `to_update/style.css`.
2. **Update styling**: Uses the `invoke` function to send the model name and its associated CSS to the `updateModelStyling` command.
3. **Error handling**: Provides feedback if the CSS file is not found or if another error occurs.

### Example usage:

```python
model_name = "Basic_Noun_Clone"
update_style(model_name)
```

Make sure `style.css` exists in the `to_update/` directory before running the script.

## Resources

- [Anki Connect Documentation](https://foosoft.net/projects/anki-connect/)

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

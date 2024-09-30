# Anki Templates Puller

A Python-based tool to fetch Anki card templates via AnkiConnect, store them as JSON files, and manage them using Git for version control.

## 🛠️ Features

- **Fetch Templates:** Retrieve all Anki note types and their card templates using AnkiConnect.
- **JSON Storage:** Store each card template as a formatted JSON file in the `card_templates/` directory.
- **Git Integration:** Automatically commit changes to a Git repository for version control.
- **Testing:** Includes a test script to verify AnkiConnect interactions.
- **Utility Modules:** Organized utilities for Git operations to keep the codebase clean and modular.

## 📋 Prerequisites

- **Anki:** Ensure Anki is installed and running on your machine.
- **AnkiConnect Add-on:** Install the [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on in Anki.
- **Python 3.7+**
- **Git:** Installed and initialized in your project directory.

## ⚙️ Installation

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

## 🚀 Usage

1. **Ensure Anki and AnkiConnect Are Running:**

   - Open Anki to activate AnkiConnect.

2. **Run the Script:**
   ```bash
   python main.py
   ```
   - This will fetch all note types, retrieve their templates, save them as JSON files in `card_templates/`, and commit any changes to the Git repository.

## 🧪 Testing

Run the test script to verify AnkiConnect's functionality:

```bash
python -m unittest discover -s test
```

## Formatting

Run the formatting script to see the card templates with proper indentation

```bash
python utils/render_json.py card_templates/Basic.json > temp.html
```

## 📈 Git Workflow

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

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 📝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

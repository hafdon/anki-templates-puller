# 🛠️ Fetch and Commit Anki Card Templates

This repository includes a Python script (`fetch_templates.py`) that fetches all your Anki card templates via AnkiConnect, saves them as JSON files, and commits any changes to the Git repository.

### 📝 Usage

1. **Ensure Prerequisites Are Met**:

   - Anki is running with the AnkiConnect add-on installed.
   - Git is installed and the repository is initialized.

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**:

   ```bash
   python fetch_templates.py
   ```

   This will fetch all note types and their card templates, save them to the `card_templates/` directory, and commit any changes to Git.

### 🔄 Automate the Process

Consider setting up a cron job or using Task Scheduler to run the script at regular intervals, ensuring your Git repository stays up-to-date with your Anki card templates.

### 📖 License

This project is licensed under the [MIT License](LICENSE).

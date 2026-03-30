
<img width="1281" height="451" alt="image" src="https://github.com/user-attachments/assets/5db07d12-8227-4d7f-b980-42aeed4e2c55" />

# PYORGANIZER
Who doesn't have any problems with a folder organization? Like a massive quantity of files in your downloads folder? 
And your solution was manually organize them, or just excluding them all.

Pyorganizer comes as an alternative, with an interactive auto folder organization(Recursively or Not) of a pre-configured folder.

**PyOrganizer** is a robust Python automation tool designed to solve the chaos of unorganized directories. Whether it's a cluttered `Downloads` folder or a massive project graveyard, PyOrganizer sorts your files into categorized folders automatically.

---

## ✨ Key Features

* **Interactive CLI:** A user-friendly terminal interface to manage settings on the fly.
* **Recursive Organization:** Choose between organizing only the final folder or diving deep into subdirectories.
* **Smart Categorization:** Automatically detects file extensions and groups them (e.g., .jpg -> JPGs).
* **Safety First:** Built with `pathlib` for cross-platform compatibility (Windows/Linux) and error handling to prevent data loss.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Core Library:** `pathlib` (Object-oriented filesystem paths)
* **System Tools:** `sys`, `os`

## 🚀 How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Caiky-Souza/pyorganizer.git
   ```
2. **Run the script:**
   ```pỳthon
   python pyorganizer.py -d seu_diretorio
   ```
3. **(ALTERNATIVE) Running interactively in CLI:**
   ```CLI
   Follow the interactive menu to set your Working Folder and Destination Folder. The default folder is Documents. You can also toggle the Recursive mode on or off (Be careful when using recursive mode on large, nested directories!).
   ```

# Kanban Terminal Project
A simple terminal-based Kanban application built in Python. 
This project allows users to add, view, and move tasks between columns on a Kanban board interactively via CLI (Command Line Interface).

---

## Feature
- Add new tasks to the "To Do" column
- View task list by column (To Do, In Progress, Done)
- Move tasks between columns
- Save and load Kanban board data persistently in JSON files

---
## Structure 
kanban_terminal/
├── main.py # CLI application entry point
├── core/ # Core modules (data model, storage, configuration)
│ ├── board.py # Board class and task management logic
│ ├── storage.py # Functions to load/save board to JSON file
│ └── config.py # Configuration, e.g. data file location
├── cli/ # CLI interface module and commands
│ ├── interface.py # Terminal interactive menu
│ ├── commands.py # Command handler functions (add, list, move)
│ └── parser.py # CLI arguments (optional)
├── utils/ # Utilities for output formatting, validation, etc
│ └── formatter.py
└── data/
└── board.json # Kanban board data storage file
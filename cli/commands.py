from core.board import Board
from core.storage import load_board, save_board
from core.config import BOARD_FILE_PATH
from rich.table import Table
from rich.console import Console

def add_task():
    board = load_board(BOARD_FILE_PATH)
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    board.add_task_to_column("To Do", title, description)
    save_board(board, BOARD_FILE_PATH)
    print("Task added.")

def list_tasks():
    board = load_board(BOARD_FILE_PATH)
    display_board_rich(board)

def move_task():
    board = load_board(BOARD_FILE_PATH)
    task_id = input("Enter task ID to move: ")
    dest_column = input("Enter destination column (To Do / In Progress / Done): ")
    board.move_task(task_id, dest_column)
    save_board(board, BOARD_FILE_PATH)
    print("Task moved.")

def delete_task():
    board = load_board(BOARD_FILE_PATH)
    column = input("Enter column name (To Do / In Progress / Done): ")
    task_id = input("Enter Task Id of the task you want to delete: ")
    if board.delete_task_from_column(column, task_id):
        save_board(board, BOARD_FILE_PATH)
        print(f"Task '{task_id}' in column '{column}' successfully deleted.")
    else:
        print("Failed to delete task.")

def display_board_rich(board):
    console = Console()
    console.print("\n[bold cyan]=== KANBAN BOARD ===[/bold cyan]")

    for column, tasks in board.columns.items():
        table = Table(title=f"[bold magenta]{column}[/bold magenta]")

        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Title", style="green")
        table.add_column("Description", style="white")

        for task in tasks:
            task_id = task.get("id", "-")
            title = task.get("title", "")
            desc = task.get("description", "")
            table.add_row(str(task_id), title, desc)

        console.print(table)


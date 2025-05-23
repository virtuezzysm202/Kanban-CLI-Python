from core.board import Board
from core.storage import load_board, save_board
from core.config import BOARD_FILE_PATH

def add_task():
    board = load_board(BOARD_FILE_PATH)
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    board.add_task_to_column("To Do", title, description)
    save_board(board, BOARD_FILE_PATH)
    print("Task added.")

def list_tasks():
    board = load_board(BOARD_FILE_PATH)
    board.display()

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
    title = input("Enter the title of the task you want to delete: ")
    if board.delete_task_from_column(column, title):
        save_board(board, BOARD_FILE_PATH)
        print(f"Task '{title}' in column '{column}' successfully deleted.")
    else:
        print("Failed to delete task.")
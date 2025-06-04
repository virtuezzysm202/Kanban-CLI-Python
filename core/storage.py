import json
from core.board import Board



def load_board(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return Board.from_dict(data)  
    except (FileNotFoundError, json.JSONDecodeError):
        return Board()

def save_board(board, file_path):
    with open(file_path, "w") as f:
        json.dump(board.to_dict(), f, indent=4)
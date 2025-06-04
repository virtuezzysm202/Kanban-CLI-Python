from rich.console import Console
from rich.table import Table

class Board:
    def __init__(self, columns=None):
        if columns is None:
            columns = {"To Do": [], "In Progress": [], "Done": []}
        self.columns = columns
        self.task_counter = self._get_max_id() + 1

    def _get_max_id(self):
        max_id = 0
        for tasks in self.columns.values():
            for task in tasks:
                if isinstance(task, dict) and task.get("id", "").isdigit():
                    max_id = max(max_id, int(task["id"]))
        return max_id

    def add_task_to_column(self, column_name, title, description):
        if column_name not in self.columns:
            print(f"Column '{column_name}' not found.")
            return False
        
        task_id = str(self.task_counter)
        task = {
            "id": task_id,
            "title": title,
            "description": description
        }

        self.columns[column_name].append(task)
        self.task_counter += 1
        print(f"Task added with ID: {task_id}")
        return True

    def move_task(self, task_id, dest_column):    
        for col, tasks in self.columns.items():
            for i, task in enumerate(tasks):
                if task.get("id") == task_id:
                    if dest_column not in self.columns:
                        print(f"Destination column '{dest_column}' not found.")
                        return False
                    self.columns[dest_column].append(task)
                    del tasks[i]
                    print(f"Task with ID '{task_id}' moved to '{dest_column}'.")
                    return True
        print(f"Task with ID '{task_id}' not found.")
        return False

    def delete_task_from_column(self, column_name, task_id):
        if column_name not in self.columns:
            print(f"Column '{column_name}' not found.")
            return False
        for i, task in enumerate(self.columns[column_name]):
            if isinstance(task, dict) and task.get("id") == task_id:
                del self.columns[column_name][i]
                print(f"Task with ID '{task_id}' deleted from '{column_name}'.")
                return True
        print(f"Task with ID '{task_id}' not found in '{column_name}'.")
        return False

    def delete_task_by_id(self, task_id):
        for column_name, tasks in self.columns.items():
            for i, task in enumerate(tasks):
                if isinstance(task, dict) and task.get("id") == task_id:
                    del tasks[i]
                    print(f"Task with ID '{task_id}' deleted from '{column_name}'.")
                    return True
        print(f"Task with ID '{task_id}' not found in any column.")
        return False

    def display(self):
        console = Console()

        todo = self.columns.get("To Do", [])
        in_progress = self.columns.get("In Progress", [])
        done = self.columns.get("Done", [])

        max_len = max(len(todo), len(in_progress), len(done))


        while len(todo) < max_len:
            todo.append(None)
        while len(in_progress) < max_len:
            in_progress.append(None)
        while len(done) < max_len:
            done.append(None)

        table = Table(title="KANBAN BOARD", show_lines=True)
        table.add_column("TO DO", style="cyan", justify="left")
        table.add_column("IN PROGRESS", style="yellow", justify="left")
        table.add_column("DONE", style="green", justify="left")

        def format_task(task):
            if task is None:
                return ""
            return f"[bold]ID:[/bold] {task['id']}\n{task['title']}\n{task['description']}"

        for i in range(max_len):
            t1 = format_task(todo[i])
            t2 = format_task(in_progress[i])
            t3 = format_task(done[i])
            table.add_row(t1, t2, t3)

        console.rule("[bold blue]KANBAN BOARD (Horizontal View)")
        console.print(table)

    @classmethod
    def from_dict(cls, data):
        columns = data.get("columns", {"To Do": [], "In Progress": [], "Done": []})
        return cls(columns)

    def to_dict(self):
        return {"columns": self.columns}

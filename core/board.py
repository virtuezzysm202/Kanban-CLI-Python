class Board:
    def __init__(self, columns=None):
        if columns is None:
            columns = {"To Do": [], "In Progress": [], "Done": []}
        self.columns = columns

    def add_task_to_column(self, column_name, title, description):
        if column_name not in self.columns:
            print(f"Column '{column_name}' None.")
            return False
        self.columns[column_name].append({"title": title, "description": description})
        return True

    def move_task(self, task_title, dest_column):
        for col, tasks in self.columns.items():
            for i, task in enumerate(tasks):
                if task['title'] == task_title:
                    if dest_column not in self.columns:
                        print(f"Destination column '{dest_column}' None.")
                        return False
                    self.columns[dest_column].append(task)
                    del tasks[i]
                    return True
        print(f"Task '{task_title}' Empty.")
        return False

    def display(self):
        for col, tasks in self.columns.items():
            print(f"\n=== {col} ===")
            if tasks:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task['title']} - {task['description']}")
            else:
                print("Task is empty.")

 
    def delete_task_from_column(self, column_name, task_title):
        if column_name not in self.columns:
            print(f"Column '{column_name}' None.")
            return False
        tasks = self.columns[column_name]
        for i, task in enumerate(tasks):
            if task['title'] == task_title:
                del tasks[i]
                return True
        return False

    @classmethod
    def from_dict(cls, data):
        columns = data.get("columns", {"To Do": [], "In Progress": [], "Done": []})
        return cls(columns)

    def to_dict(self):
        return {"columns": self.columns}

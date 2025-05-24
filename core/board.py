class Board:
    def __init__(self, columns=None):
        if columns is None:
            columns = {"To Do": [], "In Progress": [], "Done": []}
        self.columns = columns
        self.task_counter = 1 

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

    def move_task(self, task_title, dest_column):
        for col, tasks in self.columns.items():
            for i, task in enumerate(tasks):
                if task['title'] == task_title:
                    if dest_column not in self.columns:
                        print(f"Destination column '{dest_column}' not found.")
                        return False
                    self.columns[dest_column].append(task)
                    del tasks[i]
                    print(f"Task '{task_title}' moved to '{dest_column}'.")
                    return True
        print(f"Task '{task_title}' not found.")
        return False

    def clean_invalid_tasks(self):
        for col in self.columns:
            self.columns[col] = [task for task in self.columns[col] if 'id' in task]

    def display(self):
        self.clean_invalid_tasks()
        for col, tasks in self.columns.items():
            print(f"\n=== {col} ===")
            if tasks:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. [{task['id']}] {task['title']} - {task['description']}")
            else:
                print("Task is empty.")

    def delete_task_from_column(self, column_name, task_id):
        if column_name not in self.columns:
            print(f"Column '{column_name}' not found.")
            return False
        tasks = self.columns[column_name]
        for i, task in enumerate(tasks):
            if isinstance(task, dict) and 'id' in task:
                if task['id'] == task_id:
                    del tasks[i]
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

    @classmethod
    def from_dict(cls, data):
        columns = data.get("columns", {"To Do": [], "In Progress": [], "Done": []})
        return cls(columns)

    def to_dict(self):
        return {"columns": self.columns}

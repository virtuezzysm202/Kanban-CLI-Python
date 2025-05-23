# cli/interface.py
from cli.commands import add_task, list_tasks, move_task

def run_menu():
    while True:
        print("\n=== KANBAN MENU ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Move Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            move_task()
        elif choice == '4':
            print("Task Deleted")
            break
        elif choice == '5': 
            print("Goodbye")
        else:
            print("Invalid choice. Try again.")

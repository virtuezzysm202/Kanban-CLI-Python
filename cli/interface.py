from rich.table import Table
from rich.console import Console
from cli.commands import add_task, list_tasks, move_task, delete_task

def print_menu():
    table = Table(title="KANBAN MENU", show_lines=True)
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Action", style="magenta")

    menu_options = [
        ("1", "Add Task"),
        ("2", "List Tasks"),
        ("3", "Move Task"),
        ("4", "Delete Task"),
        ("5", "Exit"),
    ]

    for option, action in menu_options:
        table.add_row(option, action)

    Console().print(table)

def run_menu():
    console = Console()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            move_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            console.print("[green]Goodbye![/green]")
            break
        else:
            console.print("[red]Invalid choice. Try again.[/red]")

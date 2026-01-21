from src.storage import load_tasks, save_tasks
from src.core import show_tasks, add_task, mark_done, delete_task

def run_cli():
    tasks = load_tasks()

    while True:
        print("""
==== Todo List Cli ====
1) Show Tasks
2) Add Task
3) Mark Task Done
4) Delete Task
0) Exit
""")
        choice = input("pick an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "0":
            break
def show_tasks(tasks):
    if not tasks:
        print("\n--- No tasks found ---")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Added: {title}")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("task number: ")) - 1
        tasks[idx]["done"] = True
        print(f"Marked Done: {tasks[idx]['title']}")
    except (ValueError, IndexError):
        print("Invalid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("task number: ")) - 1
        removed = tasks.pop(idx)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid number.")
import sys
import json
from datetime import datetime
tasks = []
def main():
    global tasks
    load_task()
    try:
        if sys.argv[1] == "add" and len (sys.argv) == 3:
            description = norm_task(sys.argv[2])
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            id = generate_id()
            tasks.append({
                "id": id,
                "description": description,
                "status": "todo",
                "createdAt": date,
                "updatedAt": "-",
            })
            print(f"Task added successfully (ID: {id})")
            save_task()
        elif sys.argv[1] == "update"  and len(sys.argv) == 4:
            id = sys.argv[2]
            for task in tasks:
                if task.get("id") == id:
                    ...
                else:
                    ...
        elif sys.argv[1] == "delete" and len(sys.argv) == 3:
            #delete task
            ...
        elif sys.argv[1] == "mark-in-progress" and len(sys.argv) == 3:
            #mark-in-progress
            ...
        elif sys.argv[1] == "mark-done" and len(sys.argv) == 3:
            #mark-done
            ...
        elif sys.argv[1] == "list" and len(sys.argv) == 2:
            #list task
            ...
        elif sys.argv[1] == "list" and sys.argv[2] == "done" and len(sys.argv) == 3:
            #list done
            ...
        elif sys.argv[1] == "list" and sys.argv[2] == "todo" and len(sys.argv) == 3:
            #todo
            ...
        elif sys.argv[1] == "list" and sys.argv[2] == "in-progress" and len(sys.argv) == 3:
            #list in-progress
            ...
        else:
            print("y")
    except IndexError:
        print("y")

def norm_task(task):
    task = task.strip().lower().split()
    return " ".join(task).title()

def generate_id():
    global tasks
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1
        
def load_task():
    global tasks
    try:
        with open("task-cli.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
def save_task():
    global tasks
    with open("task-cli.json", "w") as file:
        json.dump(tasks, file, indent=4)

if __name__ == "__main__":
    main()
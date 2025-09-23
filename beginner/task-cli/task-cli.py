import sys
import json
from datetime import datetime
tasks = []
def main():
    global tasks
    load_task()
    try:
        if sys.argv[1] == "add" and len(sys.argv) == 3:  # add
            description = norm_task(sys.argv[2])

            if any(task["description"] == description for task in tasks):
                print(f"Task '{description}' already exists.")
            else:
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
        elif sys.argv[1] == "update" and len(sys.argv) == 4: #update
            id = int(sys.argv[2])
            updated = False 
            for task in tasks:
                if task["id"] == id:
                    task["description"] = norm_task(sys.argv[3])
                    task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Task {id} updated successfully")
                    updated = True
                    break
            if not updated:
                print("Task isn't available")
            save_task()
        elif sys.argv[1] == "delete" and len(sys.argv) == 3: #delete
            id = int(sys.argv[2])
            deleted = False
            for task in tasks:
                if task["id"] == id:
                    tasks.remove(task)
                    deleted = True
                    print(f"Task {id} deleted successfully")
                    break
            if not deleted:
                print("Task isn't avilable")
            save_task()
        elif sys.argv[1] == "mark-in-progress" and len(sys.argv) == 3:
            id = int(sys.argv[2])
            progress = False
            for task in tasks:
                if task["id"] == id:
                    task["status"] = "in-progress"
                    progress = True
                    print(f"Task {id} marked as in progress")
                    break
            if not progress:
                print("Task isn't available")
            save_task()
        elif sys.argv[1] == "mark-done" and len(sys.argv) == 3:
            id = int(sys.argv[2])
            done = False
            for task in tasks:
                if task["id"] == id:
                    task["status"] = "done"
                    done = True
                    print(f"Task {id} marked as done")
                    break
            if not done:
                print("Task isn't available")
            save_task()
        elif sys.argv[1] == "list" and len(sys.argv) == 2:
            for task in tasks:
                print_task(task) 

        elif sys.argv[1] == "list" and sys.argv[2] == "done" and len(sys.argv) == 3:
            for task in tasks:
                if task["status"] == "done":
                    print_task(task)

        elif sys.argv[1] == "list" and sys.argv[2] == "todo" and len(sys.argv) == 3:
            for task in tasks:
                if task["status"] == "todo":
                    print_task(task)

        elif sys.argv[1] == "list" and sys.argv[2] == "in-progress" and len(sys.argv) == 3:
            for task in tasks:
                if task["status"] == "in-progress":
                    print_task(task)
        else:
            print("""Bruhhh. usage:# Adding a new task
task-cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli.py update 1 "Buy groceries and cook dinner"
task-cli.py delete 1

# Marking a task as in progress or done
task-cli.py mark-in-progress 1
task-cli.py mark-done 1

# Listing all tasks
task-cli.py list

# Listing tasks by status
task-cli.py list done
task-cli.py list todo
task-cli.py list in-progress
""")
    except IndexError:
        print("""Bruhh, usage:# Adding a new task
task-cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli.py update 1 "Buy groceries and cook dinner"
task-cli.py delete 1

# Marking a task as in progress or done
task-cli.py mark-in-progress 1
task-cli.py mark-done 1

# Listing all tasks
task-cli.py list

# Listing tasks by status
task-cli.py list done
task-cli.py list todo
task-cli.py list in-progress
""")

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

def print_task(task):
    print(f"{task['id']}. {task['description']} is {task['status']}. "
          f"Created at {task['createdAt']} and updated at {task['updatedAt']}")

if __name__ == "__main__":
    main()
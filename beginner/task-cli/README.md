### a simple cli task manager  

this is my 2nd ever project done (backend dev). it’s a command-line task manager built with python. you can add tasks, update them, mark them as done or in-progress, delete them, and list them. all tasks are saved in a json file.  

---
## project url
<https://roadmap.sh/projects/task-tracker>

## features  
- add new tasks with unique ids  
- update task descriptions  
- delete tasks  
- mark tasks as todo, in-progress, or done  
- list tasks by status or list them all  
- prevents duplicate tasks  
- keeps track of created and updated time  

---

## installation  
1. clone the repo  
fr as i'm writing this i don't know how to do it, you know how to clone a repo?
im gonna learn git properly soon. promise


# task cli

a simple command line task manager.

## usage

add a task  
```bash
python task-cli.py add "buy groceries"


update a task

python task-cli.py update 1 "buy groceries and cook dinner"


delete a task

python task-cli.py delete 1


mark task in progress or done

python task-cli.py mark-in-progress 1
python task-cli.py mark-done 1


list tasks

python task-cli.py list
python task-cli.py list todo
python task-cli.py list in-progress
python task-cli.py list done

data format
[
  {
    "id": 1,
    "description": "buy groceries",
    "status": "todo",
    "createdAt": "2025-09-21 12:00:00",
    "updatedAt": "-"
  }
]


when a task is updated, updatedAt will be set to the current time

### end notes

this is a practice project, so don’t expect all the bells and whistles. it’s just me learning the ropes — but it’s a solid step into backend logic and file persistence.

things i picked up while building this:
how to handle command line arguments in python
how to read and write data to json files
how to prevent duplicates in a list of objects
how to keep code simple but functional
the goal here wasn’t perfection, just progress.

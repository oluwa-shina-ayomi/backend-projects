

def norm_task(task):
    task = task.strip().lower().split()
    return " ".join(task).title()


print(norm_task("  buy  Me         milk"))
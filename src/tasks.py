todo_list = []

def create_task(task):
    new_task = input("Add a task: ")
    todo_list.append(new_task)
    print (todo_list)


def delete_task(task):
    task_deleted = todo_list.remove('item')
    print (todo_list)

def mark_as_finished(task):
     for item in task:
         pass

def delete_all_tasks(task):
     pass
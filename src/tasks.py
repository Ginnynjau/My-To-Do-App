todo_list = []

#Function to create a new task
def create_task(task):
    new_task = input("Add a task: ")
    todo_list.append(new_task)
    print (todo_list)

#Function to delete a task
def delete_task(task):
    for item in task:
        todo_list.remove('item')
    print (todo_list)

#Function to mark a task as Finished
def mark_as_finished(task):
    pass

#Function that deletes all the tasks in a list
def delete_all_tasks(task):
    todo_list.clear()
    
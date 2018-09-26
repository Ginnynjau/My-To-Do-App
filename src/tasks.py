todo_list = []

#Function to create a new task
def create_task(task):
    task = input("Enter a task: ")
    if task == "":
        print("Task is BLANK. Please enter a task: ")
        return False

    todo_list.append(task)
    print("{} has been ADDED." .format(task.upper()))
    print(todo_list)
    return True
      

#Function to delete a task
def delete_task(task):
    task = input("Enter the Task Name: ")
    for item in todo_list:
        if item == task:
            todo_list.remove(task)
            print("{} has been DELETED." .format(task.upper()))
            return True
        else:    
            print("Cannot Find the Task.")
            return False
    print(todo_list)    

#Function to mark a task as Finished
def mark_as_finished(task):
    pass

#Function that deletes all the tasks in a list
def delete_all_tasks(task):
    todo_list.clear()
    print(todo_list)
    

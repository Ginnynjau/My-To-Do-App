todo_list = []

#Function to create a new task
def create_task(task):
    task = input("Enter a task: ")
    if task == "":
        print("Field is BLANK. Please enter a task: ")
        return False

    todo_list.append(task)
    print(todo_list)
    return True
      

#Function to delete a task
def delete_task(task):
    print(todo_list)
    task = int(input("Enter the task position: "))

    if task == len(todo_list):
       todo_list.remove(task)
       print("Task has been deleted.")
       print(todo_list)
    
    if task >= len(todo_list):
        print("Cannot Find the Task")
    

#Function to mark a task as Finished
def mark_as_finished(task):
    pass

#Function that deletes all the tasks in a list
def delete_all_tasks(task):
    todo_list.clear()
    print(todo_list)
    

from tasks import todo_list, create_task, delete_task, delete_all_tasks, mark_as_finished
from accounts import accounts, add_account, login

def main_menu():
    while True:
        #user options
        print("MAIN MENU")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Finished")
        print("4. Delete All Tasks")
        print("5. Quit")
               
        option = int(input("Choose a Main Menu option: "))
        if option == 1:
            print("To Add a task...")
            create_task('task')

        elif option == 2:
            print("To Delete a task...")
            delete_task('task')
        
        elif option == 3:
            print("To Mark a Finished task...")
            mark_as_finished('task')

        elif option == 4:
            print("DELETING all Tasks...")
            delete_all_tasks('task')

        elif option == 5:
            print("Exiting the To-Do list app...")
            break

        elif type(option) != int:
            print("Your Choice is Invalid. Please enter 1-5") 
            option

        else:
            print("Your Choice is Invalid. Please enter 1-5") 
            optionn
    exit

if __name__ == "__main__": 
    while True:
        answer = input("Do you have an account? Enter Y (Yes) or N (No): ")
        if answer == "N" or answer == "n" or answer == "No" :
            print ("Please sign up.")
            name = input("Enter your Username: ")
            password = input("Enter your Password: ")
            add_account(name, password)
            main_menu()
            #login('name', 'password')
            
        elif answer == "Y" or answer == "y" or answer == "Yes" :
            print("Please enter your account credentials.")
            name = input("Username: ")
            password = input("Password: ")
            login(name, password)
            if login(name, password) == True:
                main_menu()

            if login(name, password) == False:
                answer
           
        else:
            answer not in ('y', 'n', 'Y', 'N', 'Yes', 'No')
            print ("INVALID RESPONSE.")

    exit    



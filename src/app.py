from tasks import todo_list, create_task, delete_task, delete_all_tasks, mark_as_finished
from accounts import accounts, add_account, login



#Parent Class
class Users:
    def __init__(self, username, password):
        self.username = name
        self.password = password

    def add_account(self):
        pass

    def login(self):
        pass



people = [Users("Vig", "pass"), Users("njau","1234")
accounts = {}
for person in people:
    accounts[person.password] = person.name


    



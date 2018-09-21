accounts = {}

def add_account(name, password):
    accounts[password] = name

def login(name, password):
    name = input ("Username: ")
    password = input("Password: ")

    if accounts[password] is name:
        return True
    else :
        return False

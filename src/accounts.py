#Dictionary where key is the  Password and value is Username
accounts = {}

#Adds the key value pair to the accounts dictionary
def add_account(name, password):
    accounts[password] = name


#Checks if the password and corresponding Username exist in the accounts dicitionary
def login(name, password):
    name = input ("Username: ")
    password = input("Password: ")

    if accounts[password] is name:
        return True
    else:
        return False

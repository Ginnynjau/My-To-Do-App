#Dictionary where key is the  Password and value is Username
accounts = {}

#Adds the key value pair to the accounts dictionary
def add_account(name, password):
    if name != "" and password !="":
        accounts[password] = name
        print("Thank you {}, You are now a registered user." .format(name))
        return True
    else:
        print("You have enterred invalid credentials. Please sign up again.")
        return False
    print(accounts)


#Checks if the password and corresponding Username exist in the accounts dicitionary
def login(name, password):
    if name in accounts and accounts[password] == name:
        print("Welcome {}" .format(name))
        return True
    else:
        print("ERROR! The Username or Password you enterred is incorrect")
        return False


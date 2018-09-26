#Dictionary where key is the  Password and value is Username
accounts = {}

#Adds the key value pair to the accounts dictionary
def add_account(name, password):
    name = input("Enter your Username: ")
    password = input("Enter your Password: ")
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
    print("Please enter your account credentials.")
    name = input("Username: ")
    password = input("Password: ")
    if name in accounts and accounts[password] is name:
        print("Welcome {}" .format(name))
        return True
    else:
        print("ERROR! The Username or Password you enterred is incorrect")
        return False


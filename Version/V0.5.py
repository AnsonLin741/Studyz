import os
choice = ""

def login():
    global username_not_to_be_used
    global username

    username = input("Please enter your username: ")
    username_not_to_be_used = username
    file_check_L = os.path.isfile("/Versions/user.txt")
    if file_check_L == False:
        print("Username doesn't exist.")
        start()
    elif file_check_L == True:
        def passwordCheck ():
            passw_check_L = open("/Versions/user.txt" ,"r")
            passw_L = input("Please enter your passwpord.")
            if passw_check_L != passw_L:
                print("Incorrect Password. Please try again.")
                passwordCheck()
            elif passw_check_L == passw_L:
                print("Welcome " + username)
def register():
    new_user = input("Please enter a new username: ")
    file_check_R = os.path.isfile("/Versions/user.txt")
    if file_check_R == True:
        while file_check_R:
            print("This username already exist. Please enter a new one.")
            continue
    elif file_check_R == False:
        print("Your username is " + new_user)

    new_passw = input("Please enter your desired password: ")
    confirm_passw = input("Please confirm your password: ")

    if new_passw == confirm_passw:
        user_details = open("/Versions/user.txt")
        user_details.write(new_passw)
        user_details.close()
        print("Your account as been created.")

        start()

    else:
        print("Error. Please try again.")
        start()

def start():
    print("1. Login")
    print("2. Register")
    print("3. Quit")
    choice = int(input("What do you want to do?"))
    if choice == 1:
        print("Please login.")
        login()
    elif choice == 2:
        print("Please register.")
        register()
    elif choice == 3:
        print("Thank you, have a nice day.")
        quit()
    else:
        print("Invalid input. Please try again.")



start()
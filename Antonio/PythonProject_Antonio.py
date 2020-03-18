user = {}
userList = []
key = 1
import random
def mainMenu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)

def dasboardMenu():
    print("""
    1. Add Notes
    2. Edit Notes
    3. Delete Notes
    4. Add Comments
    5. Logout
    """)
    chooses = 0
    chooses = int(input("Enter Your Choice: "))
    if (chooses == 1):
        main()
    elif (chooses == 2):
        main()
    elif (chooses == 3):
        main()
    elif (chooses == 4):
        main()
    elif (chooses == 5):
        main()

def register():
    username = ""
    gender = ""
    age = 0
    while (len(username) < 5 or len(username) > 15):
        username = input("Username: ")
        username = f"{username.lower()}{random.randrange(1, 1000):03d}"
    while (gender.lower() != "male" and gender.lower() != "female" and gender.lower() != "other"):
        gender = input("Gender: ")
    while (age < 19):
        age = int(input("Age: "))
    global key
    global userList
    global user
    if username in userList:
        print("Username is Registered")
        register()
    else:
        user[key] = {"Username": username, "Age": age, "Gender": gender}
        userList.append(username)
        key+=1
        print("Register Success")
    main()

def login():
    global userList
    name = input("Username: ")
    if name.lower() in userList:
        print("Login Success")
        dasboardMenu()
    else:
        print("Could't Find Your Username")
    main()

def main():
    print(user)
    mainMenu()
    choose = 0
    while(choose < 1 or choose > 3):
        choose = int(input("Enter Your choice: "))
        if choose == 1:
            register()
        elif choose == 2:
            login()
        elif choose == 3:
            pass

if __name__ == "__main__":
    main()
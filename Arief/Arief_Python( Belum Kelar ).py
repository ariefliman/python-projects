def mainMenu():
    print("""
1. Register
2. Login
    """)

def DashBoardMenu():
    print("""
1. Add New Notes
2. Edit New Notes
3. Delete New Notes
    """)
count = None
def main():
    global count
    count = 1
    account_DB = []
    while(True):
        account = {
            "username": "",
            "gender": "",
            "age": 0,
            "password": "",
        }
        print("Notes For All")
        if account_DB == []:
            print("No Data")
        else:
            for i in account_DB:
                print(i)
        mainMenu()
        choice = int(input("Choice: "))

        if choice == 1:
            cek = 0
            print("Register Form\n")
            while(True):
                username = input("Full Name: ")
                if(5 <= len(username) <= 15):
                    if account_DB == []:
                        break
                    else:
                        for i,un in enumerate(account_DB):
                            if username in {un["username"]}:
                                print("Username Already Exist!")
                                cek = 0
                            else:
                                cek = 1
                                break
                if cek == 1: break
            
            while(True): 
                gender = input("Gender: ")
                if gender == "male" or gender == "female" or gender == "other":
                    break
                else:
                    print("Unkown Gender!")
            while(True):
                age = int(input("Age: "))
                if age >= 18 : break
                else: print("Not Enough Age!")
            password = input("Password: ")
            username = username.lower()
            username = username[:5]
            un = f"{username}{count:03d}"
            count += 1
            account["username"] = un
            account["gender"] = gender
            account["age"] = age
            account["password"] = password
            account_DB.append(account)

            print("Success Register!\nYour Username is " + un)
            input()
        if choice == 2:
            if account_DB == []: print("No Data Availabe!")
            else:
                index = -1
                username = input("Username: ")
                password = input("Password: ")
                for i,acc in enumerate(account_DB):
                    if username in {acc["username"]} and password in {acc["password"]}:
                        notes = []
                        while(True):
                            if(notes == []): print("No Data")
                            else: print(notes)
                            DashBoardMenu()
                            choice = int(input("Choice: "))
                            if choice == 1:
                                print("Create Notes: ")
                                note = input()
                                notes.append(note)
                                print("Success Add Note")
                                input()
                            elif choice == 2:
                                print("Create Notes: ")
                                note = input()
                                notes.append(note)
                                print("Success Add Note")
                                input()
                            elif choice == 3:
                                print("Delete Notes: ")
                                notes.pop(i)
                                print("Success To Delete")
                                input()
                        break
                    else:
                        print("Wrong Password or Username")
                        input()
                    

if __name__ == "__main__":
    main()
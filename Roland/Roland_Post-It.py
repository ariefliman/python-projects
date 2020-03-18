user = {}

def main():
    choice = None
    while choice != 3:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = int(input(">>"))
        if choice == 1:
            login()
        elif choice == 2:
            register()
    return

def login():
    username = input("enter username: ")
    global user
    if user.__contains__(username):
        dashboard(username)
    else:
        print("invalid username")
        return

def register():
    length = 0
    name = ""
    while length < 5 or length > 15:
        name = input("enter username[5 - 15 character]: ")
        length = len(name)
        
    name = name.lower()
    global user
    name = "%s%s" % (name, str(len(user)))
    gender = ""
    while gender != "male" and gender != "female" and gender != "other":
        gender = input("enter gender[must be male, female, or other]:")
        print(gender)
    age = 0
    while age < 18:
        age = int(input("enter age:"))
    user[name] = {"username": name, "age": age, "gender": gender, "notes": {}}
    
    

def dashboard(username):
    choice = 0
    while choice != 6:
        print("1. View by sort")
        print("2. Add Note")
        print("3. View Note")
        print("4. Remove Note")
        print("5. Add Comment")
        print("6. Main Menu")
        choice = int(input(">>"))
        if choice == 2:
            AddNote(username)
        elif choice == 3:
            ViewNote(username)
        elif choice == 4:
            global user
            if len(user[username]["notes"]) == 0:
                continue
            else:
                RemoveNote(username)
        elif choice == 5:
            AddComment(username)
        elif choice == 1:
            sortby = "none"
            while sortby != "age" and sortby != "username" and sortby != "gender":
                sortby = input("enter sort order[username|age|gender]: ")
            viewSort(username, sortby)
            
            
            
def viewSort(username, sortby):
    global user
    key = "none"
    if(sortby == "username"):
        while not user.__contains__(key):
            key = input("enter username or 0 to exit: ")
            # print(key)
            if key == "0":
                return
 
    elif sortby == "age":
        key = -1
        while key < 18:
            key = int(input("enter minimal age(bigger than 17) or 0 to exit"))
            # print(key)
            if key == 0:
                return   
    else:
        while key != "male" and key != "female" and key != "other":
            key = input("enter desired gender or 0 to quit: ")
            # print(key)
            if key == "0":
                return
        keysort = user.keys()
        keysort = sorted(keysort)
    for i in keysort:
        if user[i][sortby] != key: 
            continue
        print(i + ":")
        noteNum = len(user[i]["notes"])
        noteSorted = user[i]["notes"]
        noteSorted = sorted(noteSorted)
        for j, k in zip(range(1, noteNum + 1), noteSorted):
            print(" "*4 + str(j) + ". " + k)
            commentSorted = user[i]["notes"][k]["comment"]
            commentSorted = sorted(commentSorted)
            commentNum = len(user[i]["notes"][k]["comment"])
            for l, m in zip(range(1, commentNum + 1), commentSorted):
                print(" "*8 + str(l) + ". " + m)
    
        
        
            
            
        
        
    
def AddNote(username):
    mssg = input("enter note: ")
    global user
    user[username]["notes"][mssg] = {"content": mssg, "comment": []}
    
def ViewNote(username):
    global user
    for i in user.keys():
        note = user[i]["notes"]
        for j in note.values():
            print(j["content"])
            comment = j["comment"]
            for x in comment:
                print(" "*4 + x)
    
def RemoveNote(username):
    global user
    note = user[username]["notes"]
    num = len(note)
    for i, j in zip(range(1, num+1), note):
        print(str(i) + ". " + j)
        
    choice = -1
    while choice < 0 or choice > num:
        choice = int(input("enter note number[0-%s]: "%(str(num))))
    mssg = ""
    if choice == 0:
        return
    for i, j in zip(range(1, num+1), note):
        if i == choice:
            mssg = j
            
    note.pop(mssg)
    
def AddComment(username):
    global user
    num = 0
    for i in user.keys():
        if username != i:
            print(i + ":")
            num = len(user[i]["notes"])
            for j, k in zip(range(1, num+1), user[i]["notes"]):
                print(" "*4+ str(j) + ". " + k)
                
    choice = "EMPTY"
    while not user.__contains__(choice) or choice == username:
        choice = input("enter username or 0 to quit: ")
    
    ord = -1
    num = len(user[choice]["notes"])
    while ord < 0 or ord > num:
        ord = int(input("enter [0-%s]:"%(num)))
        
    if ord == 0:
        return
    
    mssg = ""
    for i, j in zip(range(1, num+1), user[choice]["notes"]):
        if i == ord:
            mssg = j
        
    com = input("enter comment: ")
    user[choice]["notes"][mssg]["comment"].append(com)

main()
print(user)
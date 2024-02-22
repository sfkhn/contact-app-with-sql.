import sqlite3 as sql

#MENU.
def menu():
    print("Enter 1 to add contacts.")
    print("Enter 2 to view all contacts.")
    print("Enter 3 to find a contact.")
    print("Enter 4 to update a contact.")
    print("Enter 5 to delete a contact.")
    print("Enter 6 to exit.")
    print("Enter 7 to setup.")
#EXIT MENU.

#ADD.
def add():
    db = sql.connect("C:\\Users\\sfkhn\\OneDrive\\Documents\\contact.db")
    cur = db.cursor()

    h = int(input("How many contacts: "))

    for i in range(h):
        name  = input("Enter name: ")
        ph = input("Enter ph number: ")
        
        i = "insert into contact values (?,?)"
        cur.execute(i, (name, ph))
        cur.execute("commit")
#EXIT ADD.


#VIEW.
def view():
    db = sql.connect("C:\\Users\\sfkhn\\OneDrive\\Documents\\contact.db")
    cur = db.cursor()

    res = cur.execute("select * from contact")
    for rec in res:
        print(rec) 
#EXIT VIEW.

#FIND.
def find():
    db = sql.connect("C:\\Users\\sfkhn\\OneDrive\\Documents\\contact.db")
    cur = db.cursor()

    res = cur.execute("select * from contact")
    f = input("Enter name to find contact: ")

    for rec in res:
        if f in rec:
            print(rec)
            break
    else:
        print("Contact not found!!!")
#EXIT FIND.

#UPDATE.
def update():
    db = sql.connect("C:\\Users\\sfkhn\\OneDrive\\Documents\\contact.db")
    cur = db.cursor()

    res = cur.execute("select * from contact")
    Name = input("Enter name to change contact: ")

    for rec in res:
        if Name  in rec:
            num = input("Enter new contact number: ")
            i = "update contact set PH_number=? where Name=?"
            cur.execute(i,(num,Name))#First ? name comes first.
            cur.execute("commit")
            break        
    else:
        print("Name does not exits.")
#EXIT UPDATE.

#DELETE.
def delete():
    db = sql.connect("C:\\Users\\sfkhn\\OneDrive\\Documents\\contact.db")
    cur = db.cursor()

    res = cur.execute("select * from contact")
    name = input("Enter name to delete that contact: ")

    for rec in res:
        if name in rec:
            cur.execute("delete from contact where name=?", (name,))
            #1 comma in bracket if only 1 value.
            cur.execute("commit")
            break
    else:
        print("Name does not exits.")
#EXIT DELETE.


#Main function.
while True:
    menu()
    n = int(input("Enter your choice: "))

    if n==1:
        add()
    
    elif n==2:
        view()

    elif n==3:
        find()

    elif n==4:
        update()

    elif n==5:
        delete()

    elif n==6:
        break

    elif n==7:
        db = sql.connect("C:\\Users\\sfkhn\\OneDrive\\Documents\\contact.db")
        cur = db.cursor()
        t = "create table contact (Name varchar(15), PH_number varchar(10) primary key)"
        cur.execute(t)
        
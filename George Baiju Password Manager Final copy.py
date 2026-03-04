#PASSWORD MANAGER

#Importing 
import mysql.connector as mc
from tabulate import tabulate
con=mc.connect(host="localhost",user="root",password="root")
cur=con.cursor()

global user,passw

# TABLE CREATION
try:
    cur.execute("create database passmang")
    cur.execute("use passmang")
    cur.execute("create table Users(username char(40) primary key NOT NULL,password varchar(40) NOT NULL)")
    cur.execute("create table Details(user char(40),username char(40) NOT NULL,password varchar(40) NOT NULL,sitelink varchar(70)NOT NULL)")
    con.commit()
except:
    cur.execute("use passmang")
    pass
    
# Create a new user account
def create_user(user,passw):
    values=(user,passw)
    cur.execute("INSERT INTO Users (username, password) VALUES (%s,%s)",values)   
    con.commit()
    print("Account created.")
    print("\n")
    
# Check if the user exists and the password is correct or not    
def login_user(username, password):
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username,password))
    user1=cur.fetchone()
    if user1!=None:
        print("Login Successful.")
        return True
    else:
        print("Login failed. Invalid username or password.")
    print("\n")
    

# To save a Password.
def save_pass():
    userna=input("Please enter the Username : ")
    passw=input("Please enter the Password : ")
    Website=input("Please enter the Website link : ")
    To=(user,userna,passw,Website)
    cur.execute("insert into Details value(%s,%s,%s,%s)",To)
    print("Username, Password and Website saved. ")
    con.commit()
    print("\n")
#To get a password.
def get_password(website):
    select_query = "SELECT username,password,sitelink FROM Details WHERE sitelink=%s"
    value = (website,)
    cur.execute(select_query, value)
    L=cur.fetchall()
    if L==[]:
        print("Website not found.")
    else:
        print(tabulate(L,headers=["Username", "Password","Website"],tablefmt="fancy_grid"))
    print("\n")
# Display passwords using tabulate.
def display_passwords():
    wewo=(user,)
    cur.execute("select *  from Details where user=%s",wewo)
    password=cur.fetchall()
    print(tabulate(password,headers=["User_Id","Username", "Password","Website"],tablefmt="fancy_grid"))
    print("\n")

# To delete a password.
def delete_password():
    website=input("Please enter Website link : ")
    w=(website,user)
    cur.execute("DELETE FROM Details WHERE sitelink=%s and user=%s",w)
    con.commit()
    print("Username and Password of the Website is deleted.")
    print("\n")

# To update Username.
def update_username():
    A=input("Enter current Username : ")
    newuser=input("Enter the new Username : ")
    Win=(newuser,A)
    cur.execute("UPDATE Details SET username=%s WHERE username=%s",Win)
    print("Username updated for the Website.")
    print("\n")

#To update Password.
def update_password():
    B=input("Enter the Username of the account : ")
    C=input("Enter the current Password of the account : ")
    newpassword=input("Enter the new Password : ")
    Wi=(newpassword,B,C)
    cur.execute("UPDATE Details SET password=%s WHERE username=%s and password=%s",Wi)
    print("Password updated for the Website .")
    print("\n")
# To update Sitelink.
def update_sitelink():
    D=input("Enter the Username of the account : ")
    E=input("Enter the Password of the account : ")
    newsitelink=input("Enter the new Website : ")
    N=(newsitelink,D,E)
    cur.execute("UPDATE Details SET sitelink=%s WHERE username=%s and password=%s",N)
    print("Website updated for the Website .")
    print("\n")


while True:
    print("\nᆞPᆞAᆞSᆞSᆞWᆞOᆞRᆞDᆞᆞᆞMᆞAᆞNᆞAᆞGᆞEᆞRᆞᆞᆞMᆞEᆞNᆞUᆞ ")
    print("")
    print("1- Sign Up")
    print("2- Login")
    print("3- Exit")
    choice=int(input("Enter your Choice(1/2/3) : "))
    print("\n")
    if choice==1:
        user=input("Enter Username : ")
        passw=input("Enter Password : ")
        create_user(user,passw)
        print("User created successfully!")
    elif choice==2:
        username=input("Enter your Username : ")
        password=input("Enter your Password : ")
        print("\n")
        L=login_user(username, password)
        if L==True:
            while True:
                print("---Password Manager---")
                print("1-Save a password.")
                print("2-Retrieve a password.")
                print("3-View all Username ,Password and Site link.")
                print("4-Update the Records.")
                print("5-Delete a password.")
                print("6-Exit.")
                ch=int(input("Please enter your Choice(1/2/3/4) : "))
                print("\n")
                if ch==1:
                    save_pass()
                elif ch==2:
                    website = input("Please enter website link to retrieve password :  ")
                    get_password(website)
                elif ch==3:
                    display_passwords()
                elif ch==4:
                    print("1-Change Username.")
                    print("2-Change password.")
                    print("3-Change Site Link.")
                    print("\n")
                    ch2=int(input("Enter you choice(1/2/3) : "))
                    print("\n")
                    if ch2==1:
                        update_username()
                    if ch2==2:
                        update_password()
                    if ch2==3:
                        update_sitelink()
                elif ch==5:
                    delete_password()
                elif ch==6:
                    print("You have logged out.")
                    print("\n")
                    break
    elif choice==3:
        cur.close()
        con.close()
        print("You have exited the program.")
        break

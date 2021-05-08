import csv
def registerUser():
    with open("users.csv",mode="a",newline="") as f:
        writer=csv.writer(f,delimiter=",")
        print("To register ,please enter your info:")
        email=input("Email:")
        password=input("Password: ")
        password2=input("Renter password")
        if password==password2:
            writer.writerow([email,password])
            print("You are now registered")
        else:
            print("Somethings went wrong Try again")
def loginUser():
    print("To login please enter your info:")
    email=input("Email")
    password=input("Password")
    with open("users.csv", mode="r") as  f:
        reader=csv.reader(f,delimiter=",")
        for row in reader:
            if row==[email,password]:
                print("You are logged in")
                return True
    print("Something went wrong try again")
    return False
active=True
logged_in =False
while active:
    if logged_in:
        print("1.Logout\n 2.Quit")
    else:
        print("1.Login\n 2.Register\n 3.Quit")
    choice=input("What would you like to do?").lower()
    if choice=="register" and logged_in==False:
         registerUser()
    elif choice=="login" and logged_in==False:
        logged_in=loginUser()
    elif choice=="quit":
        active=False
        print("Thanks for using our software")
    elif choice=="logout" and logged_in==True:
        logged_in=False
        print("You are logged out")
    else:
        print("Sorry,please try again")

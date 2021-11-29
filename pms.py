from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

conn = sqlite3.connect('PMS.db')
conn.execute("""CREATE TABLE IF NOT EXISTS PARKING (MOBILE CHAR(12) PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,
SEX CHAR(8) NOT NULL,EMAIL CHAR(50) NOT NULL,USERNAME CHAR(50) NOT NULL,PASSWORD CHAR(50) NOT NULL,
VEHICLE CHAR(15) NOT NULL,PARK CHAR(10) NOT NULL, TYPE CHAR(12) NOT NULL ,
STATUS CHAR(5) NOT NULL,PB CHAR(5) NOT NULL)""")
conn.commit()
conn.close()


def basePage():
    
    global root
    root=Tk()
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w,h))
    # root.configure(bg='white',bd=2)
    image = Image.open('parkLogo.png')

    # Resize the image in the given (width, height)
    img = image.resize((200, 200))

    # Convert the image in TkImage
    icon = ImageTk.PhotoImage(img)
    logo = Label(root,image=icon)
    heading = Label(root,text="PARKING MANAGEMENT SYSTEM",font=("Helvetica", 45))
    logo.grid(row=1,column=0)
    heading.grid(row=1,column=1,columnspan=2)

    # icon1=PhotoImage(file="Login.png")
    # Load the image
    image = Image.open('userLogin.png')

    # Resize the image in the given (width, height)
    img = image.resize((250,275))

    # Convert the image in TkImage
    icon1 = ImageTk.PhotoImage(img)

    log=Label(root,image=icon1)
    loginBtn=Button(root,text="Login",font=("Times New Roman",32),bd=3,command=loginPage)

    image = Image.open('NewUser.png')

    # Resize the image in the given (width, height)
    img = image.resize((250, 250))

    # Convert the image in TkImage
    icon2 = ImageTk.PhotoImage(img)
    newUser = Label(root,image=icon2)
    newUserBtn = Button(root,text="New User",font=("Times New Roman",32),bd=3,command=baseToNewUser)
    image = Image.open('Availability.png')

    # Resize the image in the given (width, height)
    img = image.resize((200, 200))

    # Convert the image in TkImage
    icon3 = ImageTk.PhotoImage(img)

    availablity=Label(root,image=icon3)
    availabilityButton=Button(root,text="Availability",font=("Times New Roman",32),bd=3,command=availability)
    log.grid(row=2)
    loginBtn.grid(row=3,column=0)
    newUser.grid(row=2,column=1)
    newUserBtn.grid(row=3,column=1)
    availablity.grid(row=2,column=2)
    availabilityButton.grid(row=3,column=2)
    root.mainloop()



def loginPage():
    root.destroy()
    global loginGUI
    loginGUI=Tk()
    loginGUI.title("Login Page")
    w,h=loginGUI.winfo_screenwidth(),loginGUI.winfo_screenheight()
    loginGUI.geometry("%dx%d+0+0" % (w,h))
    image = Image.open('parkLogo.png')

    # Resize the image in the given (width, height)
    img = image.resize((200, 200))

    # Convert the image in TkImage
    icon = ImageTk.PhotoImage(img)
    logo=Label(loginGUI,image=icon)
    heading=Label(loginGUI,text="PARKING MANAGEMENT SYSTEM",font=("Helvetica", 45))
    logo.grid(row=1,column=0)
    heading.grid(row=1,column=1,columnspan=4)
    
    lab1=Label(loginGUI,text="User Name",padx=20,pady=5,font=("Times New Roman",28))
    lab2=Label(loginGUI,text="Password",padx=20,pady=5,font=("Times New Roman",28))
    lab3=Label(loginGUI,text="\n",font=("Times New Roman",28))
    global name
    global pswd
    name=Entry(loginGUI,font=("Times New Roman",28))
    pswd=Entry(loginGUI,show="*",font=("Times New Roman",28))
    
    loginBtn=Button(loginGUI,text=" Login  ",command=validate,font=("Times New Roman",32))
    newUserBtn=Button(loginGUI,text="New User",command=loginToNewUser,font=("Times New Roman",32))
    
    lab1.grid(row=2,column=1)
    lab2.grid(row=3,column=1)
    name.grid(row=2,column=2)
    pswd.grid(row=3,column=2)
    lab3.grid(row=4)
    loginBtn.grid(row=5,column=1)
    newUserBtn.grid(row=5,column=2)
    loginGUI.mainloop()


def validate():
    flag = 0
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT USERNAME,PASSWORD FROM PARKING")
    for row in cursor:
        if ((str(name.get()) == row[0]) and (str(pswd.get()) == row[1])):
            flag = 1
            break
        else:
            flag = 0
    if (flag == 1):
        messagebox.showinfo("Status", "Login Successful")
        userPage()
    if (flag == 0):
        messagebox.showinfo("Status", "Login Failed!\nPlease Try Again.")
    conn.commit()

def loginToNewUser():
     loginGUI.destroy()
     newUserPage()

def baseToNewUser():
    root.destroy()
    newUserPage()

def newUserPage():
    global newUserGUI
    newUserGUI=Tk()
    newUserGUI.title("Login Page")
    w,h=newUserGUI.winfo_screenwidth(),newUserGUI.winfo_screenheight()
    newUserGUI.geometry("%dx%d+0+0" % (w,h))
    image = Image.open('parkLogo.png')

    # Resize the image in the given (width, height)
    img = image.resize((200, 200))

    # Convert the image in TkImage
    icon = ImageTk.PhotoImage(img)
    logo = Label(newUserGUI, image=icon)
    heading = Label(newUserGUI, text="PARKING MANAGEMENT SYSTEM", font=("Helvetica", 45))
    logo.grid(row=1,column=0)
    heading.grid(row=1,column=1,columnspan=3)
    
    lab1=Label(newUserGUI,text="Name",padx=20,pady=5,font=("Times New Roman",23))
    lab2=Label(newUserGUI,text="Gender",padx=20,pady=5,font=("Times New Roman",23))
    lab3=Label(newUserGUI,text="Mobile",padx=20,pady=5,font=("Times New Roman",23))
    lab4=Label(newUserGUI,text="Email ID",padx=20,pady=5,font=("Times New Roman",23))
    lab5=Label(newUserGUI,text="Username",padx=20,pady=5,font=("Times New Roman",23))
    lab6=Label(newUserGUI,text="Password",padx=20,pady=5,font=("Times New Roman",23))
    global Name
    global Gender
    global Mobile
    global Email
    global UserName
    global Pass
    Name=Entry(newUserGUI,font=("Times New Roman",23))
    Gender = StringVar()
    G1 = Radiobutton(newUserGUI, text="Male", variable=Gender, value="Male",font=("Times New Roman",23))
    G2 = Radiobutton(newUserGUI, text="Female", variable=Gender, value="Female",font=("Times New Roman",23))
    G3 = Radiobutton(newUserGUI, text="Other", variable=Gender, value="Other", font=("Times New Roman", 23))
    Gender.set("Male")
    Mobile = Entry(newUserGUI,font=("Times New Roman",23))
    Email = Entry(newUserGUI,font=("Times New Roman",23))
    UserName = Entry(newUserGUI,font=("Times New Roman",23))
    Pass = Entry(newUserGUI,font=("Times New Roman",23))
    lab1.grid(row=2,column=0)
    lab2.grid(row=3,column=0)
    lab3.grid(row=4,column=0)
    lab4.grid(row=5,column=0)
    lab5.grid(row=6,column=0)
    lab6.grid(row=7,column=0)
    Name.grid(row=2,column=1)
    G1.grid(row=3,column=1)
    G2.grid(row=3,column=2)
    G3.grid(row=3, column=3)
    Mobile.grid(row=4,column=1)
    Email.grid(row=5,column=1)
    UserName.grid(row=6,column=1)
    Pass.grid(row=7,column=1)

    lab7 = Label(newUserGUI,text="")
    lab7.grid(row=8)
    Submit_Button=Button(newUserGUI,text="Submit",command=dbReg,font=("Times New Roman",25),bd=3)
    Submit_Button.grid(row=9,column=1)

    newUserGUI.mainloop()

def dbReg():

    dbName = str(Name.get())
    dbMobile = str(Mobile.get())
    dbGender = str(Gender.get())
    dbEmail = str(Email.get())
    dbUsername = str(UserName.get())
    dbPass = str(Pass.get())
    dbVehicle = str("NIL")
    dbPark = str("NIL")
    dbType = str("NIL")
    dbStatus = str("Not Parked")
    dbPb = str("NIL")
    if (str(Name.get()) == "" or str(Mobile.get()) == "" or str(
            Gender.get()) == "" or str(Email.get()) == "" or str(UserName.get()) == "" or str(Pass.get()) == ""):
        messagebox.showinfo("Warning", "Fields can not be Empty!")
    else:
        conn = sqlite3.connect('PMS.db')
        conn.execute("INSERT INTO PARKING (NAME,SEX,MOBILE,EMAIL,USERNAME,PASSWORD,VEHICLE,PARK,TYPE,STATUS,PB) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(dbName,dbGender,dbMobile,dbEmail,dbUsername,dbPass,dbVehicle,dbPark,dbType,dbStatus,dbPb))
        conn.commit()
        messagebox.showinfo("Status", "Successfully Registered\nUse the Username & Password to Login")
        newUserGUI.destroy()
        basePage()

def userPage():
    loginGUI.destroy()
    global User_GUI
    User_GUI=Tk()
    w,h=User_GUI.winfo_screenwidth(),User_GUI.winfo_screenheight()
    User_GUI.geometry("%dx%d+0+0" % (w,h))
    image = Image.open('parkLogo.png')

    # Resize the image in the given (width, height)
    img = image.resize((200, 200))

    # Convert the image in TkImage
    icon = ImageTk.PhotoImage(img)
    logo = Label(User_GUI, image=icon)
    heading = Label(User_GUI, text="PARKING MANAGEMENT SYSTEM", font=("Helvetica", 45))
    logo.grid(row=1,column=0)
    heading.grid(row=1,column=1,columnspan=3)

    # icon1=PhotoImage(file="Book.png")
    # Load the image
    image = Image.open('bookNow.png')

    # Resize the image in the given (width, height)
    img = image.resize((200, 200))

    # Convert the image in TkImage
    icon1 = ImageTk.PhotoImage(img)
    Book=Label(User_GUI,image=icon1)
    BookParking_Button=Button(User_GUI,text="Book Parking",font=("Times New Roman",32),bd=3,command=bookPage)

    # Load the image
    image = Image.open('logoutUser.png')

    # Resize the image in the given (width, height)
    img = image.resize((200, 200))

    # Convert the image in TkImage
    icon3 = ImageTk.PhotoImage(img)

    Logout=Label(User_GUI,image=icon3)
    Logout_Button=Button(User_GUI,text="Logout",font=("Times New Roman",32),bd=3,command=userPageToBase)

    Y=Label(User_GUI,text="Mobile No.",font=("Times New Roman",28),padx=20,pady=5)
    global Z
    Z=Entry(User_GUI,font=("Times New Roman",28),width=11)
    Details_Button=Button(User_GUI,text="Details",font=("Times New Roman",32),bd=3,command=showDeatails)

    lab = Label(User_GUI,text="")
    lab.grid(row=2)
    Book.grid(row=3)
    BookParking_Button.grid(row=4,column=0)
    # Details.grid(row=2,column=2)
    Y.grid(row=3,column=1)
    Z.grid(row=3,column=2)
    Details_Button.grid(row=4,column=1,columnspan=2)
    Logout.grid(row=3, column=3)
    Logout_Button.grid(row=4, column=3)
    User_GUI.mainloop()
    User_GUI.mainloop()

def showDeatails():
    z=Z.get()
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT MOBILE,NAME,SEX,EMAIL,VEHICLE,PARK,TYPE,STATUS,PB  FROM PARKING")
    flag=0
    for row in cursor:
        if(row[0]==z and row[8]=="P"): # if mobile no exist & parking is booked
            msg="PARKING DETAILS : \nNAME = "+row[1]+"\nGENDER = "+row[2]+"\nMOBILE = "+row[0]+"\nEMAIL = "+row[3]+"\nVEHICLE = "+row[4]+"\nPARKING = "+row[5]+"\nCATEGORY = "+row[6]+"\nSTATUS = Booked"+"\n\n"
            messagebox.showinfo("Details", msg)
            flag=1
    if(flag==0): # if mobile no doesn't exist or parking is not booked
        msg="Invalid Mobile Number/Parking Not Booked"
        messagebox.showinfo("Note", msg)
    conn.commit()

def userPageToBase():
    messagebox.showinfo("Status","Successfully Logged Off")
    User_GUI.destroy()
    basePage()

def bookPage():
    
    User_GUI.destroy()
    global Book_GUI
    Book_GUI=Tk()
    Book_GUI.title("Book Parking")
    w, h = Book_GUI.winfo_screenwidth(),Book_GUI.winfo_screenheight()
    Book_GUI.geometry("%dx%d+0+0" % (w, h))
    image = Image.open('parkLogo.png')

    # Resize the image in the given (width, height)
    img = image.resize((200, 200))

    # Conver the image in TkImage
    icon = ImageTk.PhotoImage(img)
    logo = Label(Book_GUI, image=icon)
    PMS = Label(Book_GUI, text="PARKING MANAGEMENT SYSTEM", font=("Helvetica", 45))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=3)

    lab1=Label(Book_GUI,text="Mobile No.",padx=20,pady=5,font=("Times New Roman",32))
    lab2=Label(Book_GUI,text="Vehicle No.",padx=20,pady=5,font=("Times New Roman",32))
    lab3=Label(Book_GUI,text="Parking:",padx=20,pady=5,font=("Times New Roman",32))
    lab4=Label(Book_GUI,text="Category:",padx=20,pady=5,font=("Times New Roman",32))
    lab5=Label(Book_GUI,text="Price:",padx=20,pady=5,font=("Times New Roman",32))
    global mob
    global Veh
    mob=Entry(Book_GUI,font=("Times New Roman",32))
    Veh=Entry(Book_GUI,font=("Times New Roman",32))
    global var
    var = StringVar()

    R1 = Radiobutton(Book_GUI, text="01 Area", variable=var, value="01 Area",font=("Times New Roman",32))
    R2 = Radiobutton(Book_GUI, text="02 Area", variable=var, value="02 Area",font=("Times New Roman",32))
    R3 = Radiobutton(Book_GUI, text="03 Area", variable=var, value="03 Area",font=("Times New Roman",32))
    R4 = Radiobutton(Book_GUI, text="04 Area", variable=var, value="04 Area",font=("Times New Roman",32))
    var.set("01 Area")
    global VehTyp
    VehTyp = StringVar()
    R5 = Radiobutton(Book_GUI, text="Two Wheeler", variable=VehTyp, value="2 Wheeler", command=CalPrice2,
                     font=("Times New Roman", 32))
    R6 = Radiobutton(Book_GUI, text="Four Wheeler", variable=VehTyp, value="4 Wheeler", command=CalPrice4,
                     font=("Times New Roman", 32))
    VehTyp.set("2 Wheeler")
    
    Book_Button=Button(Book_GUI,text="Book Now",command=Park,font=("Times New Roman",32))
    
    lab1.grid(row=2,column=0)
    mob.grid(row=2,column=1)

    lab2.grid(row=3,column=0)
    Veh.grid(row=3,column=1)

    lab3.grid(row=4,column=0)
    R1.grid(row=4,column=1)
    R2.grid(row=4,column=2)

    R3.grid(row=5,column=1)
    R4.grid(row=5,column=2)
    lab4.grid(row=6, column=0)
    R5.grid(row=6,column=1)
    R6.grid(row=6,column=2)

    lab5.grid(row=7,column=0)
    global amt
    amt = Label(Book_GUI,font=("Times New Roman",32))
    amt.grid(row=7,column=1)
    
    Book_Button.grid(row=8,columnspan=2)
    
    Book_GUI.mainloop()


def CalPrice2():
        amt.config(text="300")
def CalPrice4():
        amt.config(text="500")
    

def Park():
    dbM=str(mob.get())
    dbV=str(Veh.get())
    dbA=str(var.get())
    dbT=str(VehTyp.get())
    dbS=str("Not Parked")
    dbP=str("P")
    if(str(mob.get())=="" or str(Veh.get()) =="" or str(var.get())=="" or str(VehTyp.get())==""):
        messagebox.showinfo("Warning","Fields Cannot Be Empty!")
    else:
        conn = sqlite3.connect('PMS.db')
        conn.execute("UPDATE PARKING SET VEHICLE=?,PARK=?,TYPE=?,STATUS=?,PB=? WHERE MOBILE=?", (dbV,dbA,dbT,dbS,dbP,dbM))
        conn.commit()
        conn.close()
        messagebox.showinfo("Status","Parking Successfully Booked")
        Book_GUI.destroy()
        basePage()

def availability():
    Tot01=10
    Tot02=15
    Tot03=30
    Tot04=10
    C01=0
    C02=0
    C03=0
    C04=0
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT PARK FROM PARKING")
    for row in cursor:
        if(row[0]=="02 Area"):
            C02=C02+1
        if(row[0]=="01 Area"):
            C01=C01+1
        if (row[0] == "03 Area"):
            C03 = C03 + 1
        if (row[0] == "04 Area"):
            C04 = C04 + 1
    conn.commit()
    Av02=str(Tot02-C02) #Total-number of vehicles booked in area 2
    Av01=str(Tot01-C01)
    Av03 = str(Tot03 - C03)
    Av04 = str(Tot04 - C04)
    messagebox.showinfo("Status","Total Available Parking Slots : \n\nArea 01 : "+Av01+"\n\nArea 02 : "+Av02+"\n\nArea 03 : "+Av03+"\n\nArea 04 : "+Av04)

basePage()

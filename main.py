from cProfile import label
import pathlib
from tkinter import *
from datetime import date, datetime
from PIL import ImageTk, Image
import pyrebase, tkinter
import webbrowser
import openpyxl, xlrd

firebaseConfig={'apiKey': "AIzaSyDR4ZslCMZgrl2O1DDzBgoaspzzTScCYoE",
    'authDomain': "tubes1-6911.firebaseapp.com",
    'databaseURL': "https://tubes1-6911.firebaseio.com",
    'projectId': "tubes1-6911",
    'storageBucket': "tubes1-6911.appspot.com",
    'messagingSenderId': "437693074566",
    'appId': "1:437693074566:web:25f5e30e76bf8a1dccd507",
    'measurementId': "G-Q2YCXF2SYT"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db=firebase.database(); auth=firebase.auth(); storage=firebase.storage()
# file = pathlib.Path('database.xlsx')

def showFrame(frame):
    frame.tkraise()

windowUtama = Tk()
windowUtama.state('zoomed')
# windowUtama.rowconfigure(0, weight=1)
# windowUtama.columnconfigure(0, weight=1)
windowUtama.title("Welcome to Jasamarga Tol")
width = int(windowUtama.winfo_screenwidth()); height = int(windowUtama.winfo_screenheight())
Page1 = Frame(windowUtama, width=width, height=height); Page1.grid(row=0, column=0, sticky='nsew')
Page2 = Frame(windowUtama, width=width, height=height); Page2.grid(row=0, column=0, sticky='nsew')
Page3 = Frame(windowUtama, width=width, height=height); Page3.grid(row=0, column=0, sticky='nsew')
Page4 = Frame(windowUtama, width=width, height=height); Page4.grid(row=0, column=0, sticky='nsew')
Page5 = Frame(windowUtama, width=width, height=height); Page5.grid(row=0, column=0, sticky='nsew')
# icon = Image.open('icon toll.png'); ico = ImageTk.PhotoImage(icon); Page1.wm_iconphoto(False, ico)
windowUtama.configure(bg='#f0f4fa')

showFrame(Page1)

file = openpyxl.load_workbook('database.xlsx')
fileSheet = file.sheetnames
sheet1 = file["user"]
sheet2 = file["log"]

waktu1 = datetime.now()
waktuMasuk = waktu1.strftime("%H:%M:%S")

# -- PAGE 1 -- # (Login Signup Page)

def Login():
    success = False
    try:
        auth.sign_in_with_email_and_password(loginEmail.get(), loginPass.get())
        Label(Page1, text="Logged in at " + waktuMasuk).pack()
        Label(Page1, text="Successfully logged in!").pack()
        success = True
    except:
        success = False
        failLogIn = Label(Page1, text="Either email or password are wrong"); failLogIn.pack()
    if success == True:
        showFrame(Page2)

def Signup():
    try:
        auth.create_user_with_email_and_password(signupEmail.get(), signupPass.get())
        mail = emailSignup.get(); password = passSignup.get(); saldo = saldoSignup.get()
        sheet1.cell(column=2, row=sheet1.max_row+1, value=mail)
        sheet1.cell(column=5, row=sheet1.max_row, value=password)
        sheet1.cell(column=6, row=sheet1.max_row, value=saldo)
        file.save(r'database.xlsx')
        LabelSignedUp = Label(Page1, text="Successfully created an account!"); LabelSignedUp.pack()
    except:
        failSignedUp = Label(Page1, text="Sign Up Failed"); failSignedUp.pack()

font = ("Montserrat", 10, "bold")
Label(Page1, text="Input ID", font= font).pack()
loginEmail = Entry(Page1, width=100); loginEmail.pack()
loginPass = Entry(Page1, width=100); loginPass.pack()
LoginButton = Button(Page1, text="Login", command=Login); LoginButton.pack()

emailSignup = StringVar(); passSignup = StringVar(); saldoSignup = IntVar(); saldoSignup.set('')
Label(Page1, text="Input ID", font=font).pack()
signupEmail = Entry(Page1, textvariable=emailSignup, width=100); signupEmail.pack()
signupPass = Entry(Page1, textvariable=passSignup, width=100); signupPass.pack()
# reviewSignupPass = Entry(Page1, width=100); reviewSignupPass.pack()
firstSaldo = Entry(Page1, textvariable=saldoSignup, width=100); firstSaldo.pack()
SignupButton = Button(Page1, text="Sign Up", command=Signup); SignupButton.pack()

# if reviewSignupPass.get() != signupPass:
#     PassnotSame = Label()

def firebaseconsole():
    webbrowser.open("https://console.firebase.google.com/u/0/project/tubes1-6911/authentication/users")
startButton = Button(Page1, text="Manage", command=firebaseconsole); startButton.pack()
next = Button(Page1, text="Next", command=lambda: showFrame(Page2)); next.pack()

# Label = Label(text= waktuMasuk)
# Label.pack()

#-- ACCOUNT DASHBOARD --#
def openAcc():
    dashboard = Toplevel()
    dashboard.geometry('400x500')
    dashboard.title("Account Dashboard")

    Label(dashboard, text="Account Management", font=("Montserrat", 16, 'bold')).place(x=40, y=10)
    dashboard.mainloop()

# ------ PAGE 2 ----- # (Golongan Kendaraan)


bgcolor = '#f9fbff'
Label(Page2, text="Pilih Golongan Kendaraan", font=("Montserrat", 16, "bold"), fg='#000000', bg=bgcolor, pady=10).place(x=50, y=10)
Button(Page2, text="Next", command=lambda: showFrame(Page3)).place(x=50, y=100)
accPhoto = PhotoImage(file='image/Akun.png')
user = Button(Page2, image=accPhoto, command=openAcc); user.place(x=90, y=10)


# ------ PAGE 3 ----- # (Gerbang Masuk)


Label(Page3, text="Gerbang Masuk", font=("Montserrat", 16, "bold"), fg='#000000', bg=bgcolor, pady=10).grid(row=0, column=3)

def openAcc():
    dashboard = Toplevel()
    dashboard.geometry('400x500')
    dashboard.title("Account Dashboard")
    dashboard.mainloop()

user = Button(Page3, image=accPhoto, command=openAcc); user.grid(row=0, column=6)
# text = Label(Page2, text=emailLogged); user.grid(row=0, column=7)
Label(Page3, text="Tol Semarang", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor).grid(row = 1, column = 1)

bawenPhoto = PhotoImage(file='image/Bawen.png')
semarangPhoto = PhotoImage(file='image/Semarang.png')
soloPhoto = PhotoImage(file='image/Solo.png')
tbosoPhoto = PhotoImage(file='image/Tambak Oso.png')
tbsumurPhoto = PhotoImage(file='image/Tambak Sumur.png')
juandaPhoto = PhotoImage(file='image/Juanda.png')
serpongPhoto = PhotoImage(file='image/Serpong.png')
tjpriokPhoto = PhotoImage(file='image/Tanjung Priok.png')
tmminiPhoto = PhotoImage(file='image/Taman Mini.png')

v = StringVar()
bawen = Button(Page3, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); bawen.grid(row=2, column = 1); 
semarang = Button(Page3, image=semarangPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); semarang.grid(row=2, column=2)
solo = Button(Page3, image=soloPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); solo.grid(row=2, column=3)
tboso = Button(Page3, image=tbosoPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); tboso.grid(row=4, column=1)
tbsumur = Button(Page3, image=tbsumurPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); tbsumur.grid(row=4, column=2)
juanda = Button(Page3, image=juandaPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); juanda.grid(row=4, column=3)
serpong = Button(Page3, image=serpongPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); serpong.grid(row=6, column=1)
tjpriok = Button(Page3, image=tjpriokPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); tjpriok.grid(row=6, column=2)
tmmini = Button(Page3, image=tmminiPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); tmmini.grid(row=6, column=3)

Label(Page3, text="Tol Semarang", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor).grid(row = 1, column = 1)
tol2 = Label(Page3, text="Tol Surabaya", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor).grid(row = 3, column = 1)
tol3 = Label(Page3, text="Tol Jakarta", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor).grid(row = 5, column = 1)

button = [bawen, semarang, solo, tboso, tbsumur, juanda, serpong, tjpriok, tmmini]; txtButton = ['Bawen', 'Semarang', 'Solo','Tambak Oso','Tambak Sumur','Juanda','Serpong','Tanjung Priok','Taman Mini']
def Clicked(indexTolMasuk):
    for i in range(len(button)):
        button[i]['state'] = NORMAL
    button[indexTolMasuk]['state'] = DISABLED
    global entryNumber
    entryNumber = int(indexTolMasuk)

def Submit():
    for i in range(len(button)):
        if i == entryNumber:
            hasil = Label(Page3, text=txtButton[i]); hasil.grid(row=9, column=5)

            # hasil = Label(Page2, textvariable=v, text=txtButton[i]); hasil.grid(row=7, column=5)
            gtMasuk = str(txtButton[i])
            sheet2.cell(column=2, row=sheet2.max_row, value=gtMasuk)
            file.save(r'database.xlsx')
    if entryNumber != '':
        showFrame(Page4)

bawen.config(command=lambda:Clicked(0))
semarang.config(command=lambda:Clicked(1))
solo.config(command=lambda:Clicked(2))
tboso.config(command=lambda:Clicked(3))
tbsumur.config(command=lambda:Clicked(4))
juanda.config(command=lambda:Clicked(5))
serpong.config(command=lambda:Clicked(6))
tjpriok.config(command=lambda:Clicked(7))
tmmini.config(command=lambda:Clicked(8))

submit = Button(Page3, text="Submit", command=Submit); submit.grid(row=8, column=5)


# -- PAGE 4 -- # (Gerbang Keluar)


Label(Page4, text="Gerbang Keluar", font=("Montserrat", 16, "bold"), fg='#000000', bg=bgcolor, pady=10).place(x=50, y=10)
Button(Page4, text="Next").place(x=50, y=100)

# -- PAGE 5 -- # (Saldo dan Hasil Perjalanan)

windowUtama.mainloop()
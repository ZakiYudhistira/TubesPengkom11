from cProfile import label
from tkinter import *
from datetime import date, datetime
from PIL import ImageTk, Image
import pyrebase
import webbrowser

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

db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()

def showFrame(frame):
    frame.tkraise()

windowUtama = Tk()
windowUtama.state('zoomed')
# windowUtama.rowconfigure(0, weight=1)
# windowUtama.columnconfigure(0, weight=1)
windowUtama.title("Welcome to Jasamarga Tol")
width = int(windowUtama.winfo_screenwidth()); height = int(windowUtama.winfo_screenheight())
Page1 = Frame(windowUtama, width=1466, height=720); Page1.grid(row=0, column=0, sticky='nsew')
Page2 = Frame(windowUtama, width=width, height=height); Page2.grid(row=0, column=0, sticky='nsew')
Page3 = Frame(windowUtama, width=width, height=height); Page3.grid()
# icon = Image.open('icon toll.png'); ico = ImageTk.PhotoImage(icon); Page1.wm_iconphoto(False, ico)
windowUtama.configure(bg='#f0f4fa')


showFrame(Page1)

# def NextPage():
#     global LoginPage, canvas1
#     LoginPage = Toplevel()
#     canvas1 = Canvas(LoginPage, width=width, height = height); canvas1.pack()

waktu1 = datetime.now()
waktuMasuk = waktu1.strftime("%H:%M:%S")
def Login():
    success = False
    try:
        auth.sign_in_with_email_and_password(loginEmail.get(), loginPass.get())
        timeLogin = Label(Page1, text="Logged in at " + waktuMasuk)
        timeLogin.pack()
        LabelLoggedIn = Label(Page1, text="Successfully logged in!"); LabelLoggedIn.pack()
        success = True
    except:
        success = False
        failLogIn = Label(Page1, text="Either email or password are wrong"); failLogIn.pack()
    if success == True:
        showFrame(Page2)
def Signup():
    try:
        auth.create_user_with_email_and_password(signupEmail.get(), signupPass.get())
        LabelSignedUp = Label(Page1, text="Successfully created an account!"); LabelSignedUp.pack()
    except:
        failSignedUp = Label(Page1, text="Sign Up Failed"); failSignedUp.pack()

global emailLogged, loginEmail
font = ("Montserrat", 10, "bold")
labelLogin = Label(Page1, text="Input ID", font= font); labelLogin.pack()
loginEmail = Entry(Page1, width=100); loginEmail.pack()
loginPass = Entry(Page1, width=100); loginPass.pack()
LoginButton = Button(Page1, text="Login", command=Login); LoginButton.pack()

labelSignup = Label(Page1, text="Input ID", font=font); labelSignup.pack()
signupEmail = Entry(Page1, width=100); signupEmail.pack()
signupPass = Entry(Page1, width=100); signupPass.pack()
SignupButton = Button(Page1, text="Sign Up", command=Signup); SignupButton.pack()
emailLogged = str(loginEmail.get())


def firebaseconsole():
    webbrowser.open("https://console.firebase.google.com/u/0/project/tubes1-6911/authentication/users")
startButton = Button(Page1, text="Manage", command=firebaseconsole); startButton.pack()
next = Button(Page1, text="Next", command=lambda: showFrame(Page2)); next.pack()

# Label = Label(text= waktuMasuk)
# Label.pack()


# ------ PAGE 2 ----- #


bgcolor = '#f9fbff'
judul = Label(Page2, text="Gerbang Masuk", font=("Montserrat", 16, "bold"), fg='#000000', bg=bgcolor, pady=10); judul.grid(row=0, column=3)
accPhoto = PhotoImage(file='image/Akun.png')
user = Label(Page2, image=accPhoto); user.grid(row=0, column=6)
text = Label(Page2, text=emailLogged); user.grid(row=0, column=7)
tol1 = Label(Page2, text="Tol Semarang", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor)
tol1.grid(row = 1, column = 1)

bawenPhoto = PhotoImage(file='image/Bawen.png')
semarangPhoto = PhotoImage(file='image/Semarang.png')
soloPhoto = PhotoImage(file='image/Solo.png')

bawen = Button(Page2, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); bawen.grid(row=2, column = 1); 
semarang = Button(Page2, image=semarangPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); semarang.grid(row=2, column=2)
solo = Button(Page2, image=soloPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); solo.grid(row=2, column=3)

tol2 = Label(Page2, text="Tol Jakarta", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor)
tol2.grid(row = 3, column = 1)

button = [bawen, semarang, solo]; txtButton = ['bawen', 'semarang', 'solo']
def Clicked(indexTolMasuk):
    for i in range(len(button)):
        button[i]['state'] = NORMAL
    button[indexTolMasuk]['state'] = DISABLED
    global entryNumber
    entryNumber = int(indexTolMasuk)

def Submit():
    for i in range(len(button)):
        if i == entryNumber:
            hasil = Label(Page2, text=txtButton[i]); hasil.grid(row=6, column=5)


bawen.config(command=lambda:Clicked(0))
semarang.config(command=lambda:Clicked(1))
solo.config(command=lambda:Clicked(2))

submit = Button(Page2, text="Submit", command=Submit); submit.grid(row=5, column=5)




windowUtama.mainloop()
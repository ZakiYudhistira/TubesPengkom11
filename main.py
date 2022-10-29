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



waktu1 = datetime.now()
waktuMasuk = waktu1.strftime("%H:%M:%S")

windowUtama = Tk()
width = windowUtama.winfo_screenwidth(); height = windowUtama.winfo_screenheight()
# windowUtama.geometry("%dx%d" % (width, height))
windowUtama.state('zoomed')
windowUtama.title("Welcome to Jasamarga Tol")
# icon = Image.open('icon toll.png'); ico = ImageTk.PhotoImage(icon); windowUtama.wm_iconphoto(False, ico)
windowUtama.configure(bg='#f0f4fa')


def Login():
    try:
        timeLogin = Label(windowUtama, text="Logged in at " + waktuMasuk)
        timeLogin.pack()
        auth.sign_in_with_email_and_password(loginEmail.get(), loginPass.get())
        LabelLoggedIn = Label(windowUtama, text="Successfully logged in!"); LabelLoggedIn.pack()
    except:
        failLogIn = Label(windowUtama, text="Either email or password are wrong"); failLogIn.pack()

def Signup():
    auth.create_user_with_email_and_password(signupEmail.get(), signupPass.get())
    LabelSignedUp = Label(windowUtama, text="Successfully created an account!"); LabelSignedUp.pack()

font = ("Montserrat", 10, "bold")
labelLogin = Label(text="Input ID", font= font); labelLogin.pack()
loginEmail = Entry(width=100); loginEmail.pack()
loginPass = Entry(width=100); loginPass.pack()
LoginButton = Button(windowUtama, text="Login", command=Login); LoginButton.pack()

labelSignup = Label(text="Input ID", font=font); labelSignup.pack()
signupEmail = Entry(width=100); signupEmail.pack()
signupPass = Entry(width=100); signupPass.pack()
SignupButton = Button(windowUtama, text="Sign Up", command=Signup); SignupButton.pack()

def firebaseconsole():
    webbrowser.open("https://console.firebase.google.com/u/0/project/tubes1-6911/authentication/users")
startButton = Button(windowUtama, text="Manage", command=firebaseconsole); startButton.pack()

# Label = Label(text= waktuMasuk)
# Label.pack()



windowUtama.mainloop()
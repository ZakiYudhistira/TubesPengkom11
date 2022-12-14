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
windowUtama.title("Welcome to Jasamarga Tol")
width = windowUtama.winfo_screenwidth(); height = windowUtama.winfo_screenheight()
Page1 = Frame(windowUtama, width=width, height=height); Page1.pack()
Page2 = Frame(windowUtama, width=width, height=height); Page2.pack()
Page3 = Frame(windowUtama, width=width, height=height); Page3.pack()
# icon = Image.open('icon toll.png'); ico = ImageTk.PhotoImage(icon); Page1.wm_iconphoto(False, ico)
windowUtama.configure(bg='#f0f4fa')

# def NextPage():
#     global LoginPage, canvas1
#     LoginPage = Toplevel()
#     canvas1 = Canvas(LoginPage, width=width, height = height); canvas1.pack()

waktu1 = datetime.now()
waktuMasuk = waktu1.strftime("%H:%M:%S")
def Login():
    # global success
    success = False
    try:
        timeLogin = Label(Page1, text="Logged in at " + waktuMasuk)
        timeLogin.pack()
        auth.sign_in_with_email_and_password(loginEmail.get(), loginPass.get())
        LabelLoggedIn = Label(Page1, text="Successfully logged in!"); LabelLoggedIn.pack()

    except:
        failLogIn = Label(Page1, text="Either email or password are wrong"); failLogIn.pack()
        success = False
    # if success == True:
    #     lambda: show_frame(canvas1)

def Signup():
    auth.create_user_with_email_and_password(signupEmail.get(), signupPass.get())
    LabelSignedUp = Label(Page1, text="Successfully created an account!"); LabelSignedUp.pack()

font = ("Montserrat", 10, "bold")
labelLogin = Label(Page1, text="Input ID", font= font); labelLogin.pack()
loginEmail = Entry(Page1, width=100); loginEmail.pack()
loginPass = Entry(Page1, width=100); loginPass.pack()
LoginButton = Button(Page1, text="Login", command=Login); LoginButton.pack()

labelSignup = Label(Page1, text="Input ID", font=font); labelSignup.pack()
signupEmail = Entry(Page1, width=100); signupEmail.pack()
signupPass = Entry(Page1, width=100); signupPass.pack()
SignupButton = Button(Page1, text="Sign Up", command=Signup); SignupButton.pack()

def firebaseconsole():
    webbrowser.open("https://console.firebase.google.com/u/0/project/tubes1-6911/authentication/users")
startButton = Button(Page1, text="Manage", command=firebaseconsole); startButton.pack()
next = Button(Page1, text="Next", command=lambda: showFrame(Page2)); next.pack()

# Label = Label(text= waktuMasuk)
# Label.pack()
bgcolor = '#f9fbff'
judul = Label(Page2, text="Gerbang Masuk", font=("Montserrat", 16, "bold"), fg='#000000', bg=bgcolor, pady=10); judul.grid(row=0, column=3)
tol1 = Label(Page2, text="Tol Semarang", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor)
tol1.grid(row = 1, column = 1); bawenPhoto = PhotoImage(file='image/Bawen.png')
bawen = Button(Page2, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); bawen.grid(row=2, column = 1); 
semarang = Button(Page2, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); semarang.grid(row=2, column=2)
solo = Button(Page2, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); solo.grid(row=2, column=3)

tol2 = Label(Page2, text="Tol Jakarta", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor)
tol2.grid(row = 3, column = 1)

button = [bawen, semarang, solo]; txtButton = ['bawen', 'semarang', 'solo']
def Clicked(ind):
    for i in range(len(button)):
        button[i]['state'] = NORMAL
    button[ind]['state'] = DISABLED
    global entryNumber
    entryNumber = int(ind)

def Submit():
    for i in range(len(button)):
        if i == entryNumber:
            hasil = Label(Page2, text=txtButton[i]); hasil.grid(row=6, column=5)


bawen.config(command=lambda:Clicked(0))
semarang.config(command=lambda:Clicked(1))
solo.config(command=lambda:Clicked(2))

submit = Button(Page2, text="Submit", command=Submit); submit.grid(row=5, column=5)




windowUtama.mainloop()
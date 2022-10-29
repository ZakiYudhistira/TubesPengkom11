from tkinter import *
import customtkinter
from datetime import date, datetime
from PIL import ImageTk, Image
import pyrebase

entry = Tk()
bgcolor = '#f9fbff'
entry.config(bg=bgcolor)
entry.state('zoomed')
width = entry.winfo_screenwidth(); height = entry.winfo_screenheight()

judul = Label(entry, text="Gerbang Masuk", font=("Montserrat", 16, "bold"), fg='#000000', bg=bgcolor, pady=10); judul.grid(row=0, column=3)
tol1 = Label(entry, text="Tol Semarang", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor)
tol1.grid(row = 1, column = 1); bawenPhoto = PhotoImage(file='image/Bawen.png')
bawen = Button(entry, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); bawen.grid(row=2, column = 1); 
semarang = Button(entry, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); semarang.grid(row=2, column=2)
solo = Button(entry, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); solo.grid(row=2, column=3)

tol2 = Label(entry, text="Tol Jakarta", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor)
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
            hasil = Label(entry, text=txtButton[i]); hasil.grid(row=6, column=5)


bawen.config(command=lambda:Clicked(0))
semarang.config(command=lambda:Clicked(1))
solo.config(command=lambda:Clicked(2))

submit = Button(entry, text="Submit", command=Submit); submit.grid(row=5, column=5)



entry.mainloop()

# app = Tk()
# def switchButton():
#     if button1['state'] == NORMAL:
#         button1['state'] = DISABLED
#     else:
#         button1['state'] = NORMAL


# button1 = Button(app, text="Button1", state=DISABLED); button1.pack()
# button2 = Button(app, text="Button2", command=switchButton); button2.pack()
# app.mainloop()

from tkinter import *
import customtkinter
from datetime import date, datetime
from PIL import ImageTk, Image
import pyrebase

exit = Tk()
bgcolor = '#f9fbff'
exit.config(bg=bgcolor)
exit.state('zoomed')
width = exit.winfo_screenwidth(); height = exit.winfo_screenheight()

judul = Label(exit, text="Gerbang Keluar", font=("Montserrat", 16, "bold"), fg='#000000', bg=bgcolor, pady=10); judul.grid(row=0, column=3)
tol1 = Label(exit, text="Tol Semarang", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor)
tol1.grid(row = 1, column = 1); bawenPhoto = PhotoImage(file='image/Bawen.png')
bawen = Button(exit, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); bawen.grid(row=2, column = 1); 
semarang = Button(exit, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); semarang.grid(row=2, column=2)
solo = Button(exit, image=bawenPhoto, borderwidth=0, bg=bgcolor, padx=5, state=NORMAL); solo.grid(row=2, column=3)

tol2 = Label(exit, text="Tol Jakarta", font=("Montserrat", 13, 'bold'),  fg='#000000', bg=bgcolor)
tol2.grid(row = 3, column = 1)

button = [bawen, semarang, solo]; txtButton = ['bawen', 'semarang', 'solo']
print(exitNumber)
def Clicked(ind):
    for i in range(len(button)):
        button[i]['state'] = NORMAL
    button[ind]['state'] = DISABLED
    global exitNumber, txt
    exitNumber = int(ind)

def Submit():
    for i in range(len(button)):
        if i == exitNumber:
            hasil = Label(exit, text=txtButton[i]); hasil.grid(row=6, column=5)


bawen.config(command=lambda:Clicked(0))
semarang.config(command=lambda:Clicked(1))
solo.config(command=lambda:Clicked(2))

submit = Button(exit, text="Submit", command=Submit); submit.grid(row=5, column=5)


exit.mainloop()
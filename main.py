from tkinter import *
from datetime import date, datetime
from PIL import ImageTk, Image

waktu1 = datetime.now()
waktuMasuk = waktu1.strftime("%H:%M:%S")

windowUtama = Tk()
width = windowUtama.winfo_screenwidth(); height = windowUtama.winfo_screenheight()
windowUtama.geometry("%dx%d" % (width, height))
windowUtama.title("Welcome to Jasamarga Tol")
icon = Image.open('icon toll.png'); ico = ImageTk.PhotoImage(icon); windowUtama.wm_iconphoto(False, ico)
windowUtama.configure(bg='#f0f4fa')


# Label = Label(text= waktuMasuk)
# Label.pack()


windowUtama.mainloop()
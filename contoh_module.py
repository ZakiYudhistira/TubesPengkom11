from tkinter import *
dashboard = Tk()
dashboard.geometry('400x500')
dashboard.title("Account Dashboard")
Label(dashboard, text="Account Management", font=("Montserrat", 16, 'bold')).place(x=40, y=10)
Label(dashboard, text="Email", font=("Calibri", 12, 'bold')).place(x=40, y=70)
Label(dashboard, text="bagas@mail", font=("Calibri", 12), padx = 10, bg='#f9fbff').place(x=100, y=70)
dashboard.mainloop()
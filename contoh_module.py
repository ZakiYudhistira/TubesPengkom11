from tkinter import *
dashboard = Tk()
dashboard.state('zoomed')
dashboard.title("Account Dashboard")
Label(dashboard, text="Biaya Perjalanan", font=("Montserrat", 60, 'bold')).place(x=180, y=70)
Label(dashboard, text="12.000", font=("Montserrat", 50, 'bold')).place(x=180, y=170)
Button(dashboard, text="Submit", font=("Lato", 15, 'bold'), padx=12, pady=3).place(x=1466/2, y=720-100)
# Label(dashboard, text="bagas@mail", font=("Calibri", 12), padx = 10).place(x=100, y=70)
dashboard.mainloop()
from tkinter import *
dashboard = Tk()
dashboard.state('zoomed')
dashboard.title("Account Dashboard")
width = int(dashboard.winfo_screenwidth()); height = int(dashboard.winfo_screenheight())
Label(dashboard, text="Saldo Anda sisa : " + str(69000), font=("Montserrat", 15, 'bold')).place(x=width/2-95, y=800)
Label(dashboard, text="Semoga Selamat Sampai Tujuan", font=("Montserrat", 15, 'bold')).place(x=width/2-135, y=800)
end = Button(dashboard, text="Submit", font=("Lato", 15, 'bold'), padx=12, pady=3, state=NORMAL); end.place(x=width/2 - 20, y=height-200)
dashboard.mainloop()
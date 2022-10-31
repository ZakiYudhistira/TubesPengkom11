from tkinter import *
dashboard = Tk()
dashboard.state('zoomed')
dashboard.title("Account Dashboard")
width = int(dashboard.winfo_screenwidth()); height = int(dashboard.winfo_screenheight())
Label(dashboard, text="Saldo Anda sisa : " + str(69000), font=("Montserrat", 15, 'bold')).place(x=width/2-95, y=800)
Label(dashboard, text="Semoga Selamat Sampai Tujuan", font=("Montserrat", 15, 'bold')).place(x=width/2-135, y=800)
end = Button(dashboard, text="Submit", font=("Lato", 15, 'bold'), padx=12, pady=3, state=NORMAL); end.place(x=width/2 - 20, y=height-200)
Label(dashboard, text="Jarak : ", font=("Montserrat", 20, 'bold')).place(x=180, y=275)
Label(dashboard, text=200, font=("Courier", 20, 'bold')).place(x=280, y=275)
Button(dashboard, text="Keluar Tol", font=("Lato", 20, 'bold'),padx=40, pady=25).place(x=180, y=460)
Label(dashboard, text="Saldo Anda sisa : Rp." + str(12000), font=("Montserrat",20, 'bold')).place(x=180, y=400)
Label(dashboard, text="Semoga Selamat Sampai Tujuan !", font=("Montserrat", 20, 'bold')).place(x=180, y=350)


dashboard.mainloop()
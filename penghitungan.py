# import tkinter
# from entry import entryNumber
# from exit import exitNumber
# import pyrebase

# firebaseConfig={'apiKey': "AIzaSyDR4ZslCMZgrl2O1DDzBgoaspzzTScCYoE",
#     'authDomain': "tubes1-6911.firebaseapp.com",
#     'databaseURL': "https://tubes1-6911.firebaseio.com",
#     'projectId': "tubes1-6911",
#     'storageBucket': "tubes1-6911.appspot.com",
#     'messagingSenderId': "437693074566",
#     'appId': "1:437693074566:web:25f5e30e76bf8a1dccd507",
#     'measurementId': "G-Q2YCXF2SYT"
# }
# firebase = pyrebase.initialize_app(firebaseConfig)

# db=firebase.database()
# auth=firebase.auth()
# storage=firebase.storage()

# windowHitung = Tk()

# entryNumber = 2; exitNumber = 4

# def Jarak(entryNumber, exitNumber):
#     global jarak
#     Semarang_tol = (["Bawen",23.1],
#                     ["Semarang",0],
#                     ["Solo",40])
#     Jakarta_tol = ( ["Tanjung Priok",12.1],
#                     ["Serpong",10.1],
#                     ["Taman Mini",4.5])
#     Surabaya_tol =( ["Juanda",12.8],
#                     ["Tambak Sumur",5],
#                     ["Tambak Oso",9])
#     if entryNumber <= 2:
#         entryTol = Semarang_tol[entryNumber]
#     elif 3 < entryNumber <= 5:
#         entryTol = Jakarta_tol[entryNumber]
#     elif 6 < entryNumber <= 8:
#         entryTol = Surabaya_tol[entryNumber]

#     if exitNumber <= 2:
#         exitTol = Semarang_tol[exitNumber]
#     elif 3 < exitNumber <= 5:
#         exitTol = Jakarta_tol[exitNumber]
#     elif 6 < exitNumber <= 8:
#         exitTol = Surabaya_tol[exitNumber]

#     Semarang = False
#     Jakarta = False
#     Surabaya = False
#     jarak = 0
#     for i in range(3):
#         if entryTol == Semarang_tol[i][0]:
#             jarak = jarak + Semarang_tol[i][1]
#             Semarang = True
#         if entryTol == Jakarta_tol[i][0]:
#             jarak = jarak + Jakarta_tol[i][1]
#             Jakarta = True
#         if entryTol == Surabaya_tol[i][0]:
#             jarak = jarak + Surabaya_tol[i][1]
#             Surabaya = True
#     for j in range(3):
#         if exitTol == Semarang_tol[j][0]:
#             jarak = jarak + Semarang_tol[j][1]
#             Semarang = True
#         if exitTol == Jakarta_tol[j][0]:
#             jarak = jarak + Jakarta_tol[j][1]
#             Jakarta = True
#         if exitTol == Surabaya_tol[j][0]:
#             jarak = jarak + Surabaya_tol[j][1]
#             Surabaya = True
#     if Surabaya == True and Jakarta == True:
#         jarak = jarak + 797
#     elif Surabaya == True and Semarang == True:
#         jarak = jarak + 351
#     elif Jakarta == True and Semarang == True:
#         jarak = jarak + 446
#     return (jarak)

# jarakHasil = Label(windowHitung, text=jarak); jarakHasil.pack()
# windowHitung.mainloop()
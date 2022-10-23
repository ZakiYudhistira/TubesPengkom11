# ini kode buat jarak nyimpen database jarak tol
# Jakarta -- Semarang 446 KM
# Semarang -- Surabaya 351 KM
entry1 = input("Masukkan tol anda masuk : ")
exit1 = input("Masukkan tol anda keluar : ")
Semarang_tol = (["Bawen",23.1],
                ["Semarang",0],
                ["Solo",40])
Jakarta_tol = ( ["Tanjung Priok",12.1],
                ["Serpong",10.1],
                ["Taman Mini",4.5])
Surabaya_tol =( ["Juanda",12.8],
                ["Tambak Sumur",5],
                ["Tambak Oso",9])
Semarang = False
Jakarta = False
Surabaya = False
jarak = 0
for i in range(3):
    if entry1 == Semarang_tol[i][0]:
        jarak = jarak + Semarang_tol[i][1]
        Semarang = True
    if entry1 == Jakarta_tol[i][0]:
        jarak = jarak + Jakarta_tol[i][1]
        Jakarta = True
    if entry1 == Surabaya_tol[i][0]:
        jarak = jarak + Surabaya_tol[i][1]
        Surabaya = True
for j in range(3):
    if exit1 == Semarang_tol[j][0]:
        jarak = jarak + Semarang_tol[j][1]
        Semarang = True
    if exit1 == Jakarta_tol[j][0]:
        jarak = jarak + Jakarta_tol[j][1]
        Jakarta = True
    if exit1 == Surabaya_tol[j][0]:
        jarak = jarak + Surabaya_tol[j][1]
        Surabaya = True
if Surabaya == True and Jakarta == True:
    jarak = jarak + 797
elif Surabaya == True and Semarang == True:
    jarak = jarak + 351
elif Jakarta == True and Semarang == True:
    jarak = jarak + 446
print(f"Total jarak yang ditempuh adalah {jarak}")

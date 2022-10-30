# ini kode buat jarak nyimpen database jarak tol
# Jakarta -- Semarang 446 KM
# Semarang -- Surabaya 351 KM
from cgi import test


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
tarifentry = 0
tarifexit = 0
for i in range(3):
    if entry1 == Semarang_tol[i][0]:
        jarak = jarak + Semarang_tol[i][1]
        Semarang = True
        tarifentry = Semarang_tol[i][1]*400
    if entry1 == Jakarta_tol[i][0]:
        jarak = jarak + Jakarta_tol[i][1]
        Jakarta = True
        tarifentry = Jakarta_tol[i][1]*300
    if entry1 == Surabaya_tol[i][0]:
        jarak = jarak + Surabaya_tol[i][1]
        Surabaya = True
        tarifentry = Surabaya_tol[i][1]*450
for j in range(3):
    if exit1 == Semarang_tol[j][0]:
        jarak = jarak + Semarang_tol[j][1]
        Semarang = True
        tarifexit = Semarang_tol[j][1]*400
    if exit1 == Jakarta_tol[j][0]:
        jarak = jarak + Jakarta_tol[j][1]
        Jakarta = True
        tarifexit = Jakarta_tol[j][1]*300
    if exit1 == Surabaya_tol[j][0]:
        jarak = jarak + Surabaya_tol[j][1]
        Surabaya = True
        tarifexit = Surabaya_tol[j][1]*450
if Surabaya == True and Jakarta == True:
    jarak = jarak + 797
elif Surabaya == True and Semarang == True:
    jarak = jarak + 351
elif Jakarta == True and Semarang == True:
    jarak = jarak + 446
print(f"Total jarak yang ditempuh adalah {jarak}")

# Tarif Jakarta - Semarang : I=800 II=1200 III=1600
# Tarif Semarang - Surabaya : I = 950 II=1450 III=1900
#Tarif subtol Jakarta = 300
#Tarif subtol Semarang = 400
#Tarif subtol Surabaya =450
def hitungtarifmobil(tarifentry,tarifexit): 
    if Surabaya == True and Jakarta == True:
        hasil = (351*950) + (446*800) + tarifentry + tarifexit
    elif Surabaya == True and Semarang == True :
        hasil = (351*950) + tarifentry + tarifexit
    elif Jakarta == True and Semarang == True :
        hasil = (446*800) + tarifentry + tarifexit
    return hasil
def hitungtarifbus(tarifentry,tarifexit):
    if Surabaya == True and Jakarta == True:
        hasil = (351*1450) + (446*1200) + tarifentry + tarifexit
    elif Surabaya == True and Semarang == True :
        hasil = (351*1450) + tarifentry + tarifexit
    elif Jakarta == True and Semarang == True :
        hasil = (446*1200) + tarifentry + tarifexit
    return hasil
def hitungtariftruk(tarifentry,tarifexit):
    if Surabaya == True and Jakarta == True:
        hasil = (351*1900) + (446*1200) + tarifentry + tarifexit
    elif Surabaya == True and Semarang == True :
        hasil = (351*1900) + tarifentry + tarifexit
    elif Jakarta == True and Semarang == True :
        hasil = (446*1600) + tarifentry + tarifexit
    return hasil
# Mobil Pribadi = I
# Bus = II
# Truk = III
def hitungtarif(Golongan):
    if Golongan == 'I':
        tarif = hitungtarifmobil(tarifentry,tarifexit)
    elif Golongan == 'II':
        tarif = hitungtarifbus(tarifentry,tarifexit)
    elif Golongan == 'III':
        tarif = hitungtariftruk(tarifentry,tarifexit)
    return tarif

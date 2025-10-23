# Tsüklid (FOR, WHILE, WHILE True)
# Proovi lahendada kõik ülesanded kolme erineva tsükliga, kui see on võimalik.
# 1️⃣ Sisestatakse 15 arvu.
# Määrata, mitu neist on täisarvud.
'''k=0 #loendur
for i in range(15):
    arv=float(input(f"Sisesta arv:{i+1} "))
    if int(arv)==arv:
        print(f"{arv} on täisarv")
        k+=1
    else:
        print(f"{arv} ei ole täisarv")
3
print(f"Sisestatud arvudest on {k} täisarvu")'''

#2️ Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.

'''A=int(input("Sisesta arv A: "))
summa=0
for i in range(1,A+1):
    summa+=i
    print(f"Arvude summa vahemikus 1 kuni {A} on {summa}")'''

#3️ Sisestatakse 8 arvu.
#Leida nende korrutis (ainult positiivsete arvude puhul).
'''try:
    for i in range(8):
        arv=float(input(f"Sisesta arv:{i+1} "))
        if arv>0: 
            arv = arv * arv
        else:
            pass
    print(f"Kõigi positiivsete arvude korrutis on {arv}")
except:
    print("Sisesta ainult numbreid")'''

#4️ Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.
'''
    for i in range(10,21):
        ruut=i**2
        print(f"Arvu {i} ruut on {ruut}")
'''

# 5️ Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
# N väärtus sisestatakse klaviatuurilt.

'''try: 
    N = int(input("Sisesta arvude hulk N: "))
    
    print("Sisesta positivne arv")
    summa = 0
    if N > 0:
        for i in range(N):
            arv = float(input(f"Sisesta arv {i + 1}: "))
            if arv < 0:
                summa += arv
        print(f"Negatiivsete arvude summa on: {summa}")
    else:
        print("Sisesta positiivne arv")
    
except:
    print("Sisesta ainult numbreid")'''

# 6️ Klaviatuurilt sisestatakse N arvu.
# Koosta programm, mis määrab sisestatud arvude seast:

# negatiivsete arvude arvu,

# positiivsete arvude arvu,

# nullide arvu.
# (N väärtus sisestatakse klaviatuurilt.)
'''try:
    N = int(input("Sisesta arvude hulk N: "))
    negatiivne = 0
    positiivne = 0
    nullid = 0
    if N > 0:
        for i in range(N):
            arv = float(input(f"Sisesta arv {i + 1}: "))
            if arv < 0:
                negatiivne += 1
            elif arv > 0:
                positiivne += 1
            else:
                nullid += 1
        print(f"Negatiivsete arvude arv on: {negatiivne}")
        print(f"Positiivsete arvude arv on: {positiivne}")
        print(f"Nullide arv on: {nullid}")
    else:
        print("Sisesta positiivne arv")
except:
    print("Sisesta ainult numbreid")'''

# 7️ Väljastada ekraanile arvud, mis on K-ga jaguvad vahemikust [A, B].

'''try:
    a = int(input("Sisesta algus arv A: "))
    b = int(input("Sisesta lõppus arv B: "))
    K = int(input("Sisesta jagaja K: "))
    for i in range(a, b + 1):
        if i % K == 0:
            print(f"Arv {i} on jaguv K-ga")
except:
    print("sisesta ainult arv")'''

#8️ Koosta programm, mis prindib tollide ja sentimeetrite teisendustabeli
#(1 toll = 2,5 cm) väärtuste jaoks 1 kuni 20 tolli.

'''print("Tollid\tSentimeetrid")
for toll in range(1, 21):
    sentimeetrid = toll * 2.5
    print(f"{toll}\t{sentimeetrid:.2f}") # t joondab teksti veerus'''

#9️ Panka pandi S eurot 3% intressiga.
#Määrata, kui suureks summa muutub N aasta järel.

S = float(input("Sisesta algne summa S eurodes: "))
N = int(input("Sisesta aastate: "))







            


    

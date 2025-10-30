# 1️ Kirjuta programm, mis antud arvu n (1–9) põhjal kuvab ekraanile n jänest.
#Kahe jänese vahel peab olema tühikurida (veerg tühikutega).
#Lubatud on lisada tühikurida ka pärast viimast jänest.
#Kopeeri jänese kuju arenduskeskkonda.

#   (\_/)
#   (o o)
#   / | \*

'''try:
    n = int(input("Sisesta arv vahemikus 1-9: "))
    jänes = [
                "(\_/)\t", 
                "(o o)\t", 
               "/ | \*\t",
                 ]
    if 1 <= n <= 9:
        for line in jänes:
            print(line * n, end='  ')
            print()
except:
    print("Palun sisesta korrektne arv vahemikus 1-9.") '''


 # 2 Arvuta arvude summa 0 kuni L (kaasa peetakse). Näide: 0+1+2+3+…+14.
'''try:
    L = int(input("Sisesta arv L: "))
    summa = 0
    for i in range(L + 1):
        summa += i
        print("Arvude summa 0 kuni", L, "on:", summa)
except:
    print("Palun sisesta korrektne arv.")'''


# 3  Programmis genereeritud juhuslik täisarv esineb 0–100.
#Kasutaja peab selle ära arvama mitte rohkem kui 10 katsega.
#Pärast iganud katset teavitab programm, mida sisestatud arv on suurem või väiksem otsitavast.
#Kui 10 katsega ei arva ära, kuvab programm õige vastuse.
'''import random
try:
    randomarv = random.randint(0, 100)
    katseid = 0
    user = int(input("Arva ära juhuslikult genereeritud arv vahemikus 0-100: "))

    while katseid <= 10:
        katseid += 1
        if user > 100 or user < 0:
            print("Arv peab olema vahemikus 0-100.")
            user = int(input("Proovi uuesti: "))
            continue
        if user > randomarv:
            print(" arv on väiksem")
            user = int(input("Proovi uuesti: "))
        elif user < randomarv:
            print(" arv on suurem ")
            user = int(input("Proovi uuesti: "))
        else:
            print("Õige vastus on:", randomarv)
            print("Palju õnne! Arvasid arvu ära", katseid, "katsega.")
            break
except:
    print("Palun sisesta korrektne arv.")'''

# 4 Moodusta sisestatud arvust ümberpööratud arv ja kuva see ekraanile.
#Näide: 3486 → 6843.
'''try:
    a = int(input("sisesta numbrid:  "))
except:
        print("Palun sisesta korrektne arv.")
b = str(a)
b = reversed(b)
for i in b:
    print(i, end="")'''


# 5️ Leia sisestatud täisarvu numbrite summa ja korrutis.
# Näide: 325 → summa = 10 (3+2+5), korrutis = 30 (3×2×5).

'''try:
    arv = int(input("Sisesta täisarv: "))
    summa = 0
    korrutis = 1
    for number in str(arv):
        summa += int(number)
        korrutis *= int(number)
    print("Numbrite summa on:", summa)
    print("Numbrite korrutis on:", korrutis)
except:
    print("Palun sisesta korrektne täisarv.")'''






    
            

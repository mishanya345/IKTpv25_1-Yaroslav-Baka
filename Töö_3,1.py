
# Tsüklid (FOR, WHILE, WHILE True)
# Proovi lahendada kõik ülesanded kolme erineva tsükliga, kui see on võimalik.
# Sisestatakse 15 arvu.
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

'''s = int(input('sisesta sinu hind:'))
n = int(input("sisesta mittu aastat:"))

r = 0.03

summa = s*(1+r)**n # see on formula rasked protsenti

print(f"summa on {summa:.2f}")'''

#10 Klaviatuurilt sisestatakse 10 arvu paari.
#Võrdle igas paaris olevaid arve ja väljasta neist suurem arv.
'''try:
    for i in range(10):
        print(f"arvupaar {i+1}:")
        arv1 = int(input("sisesta esimene arv"))
        arv2 = int(input("sisesta teine arv"))
        if int(arv1) and int(arv2):  
            suurem = max(arv1, arv2)
            print(f"suurem arv on {suurem}:\n")
        else:
            pass
except:
    print("kirjuta ainult täisarv")'''
    
#11 Leia kahekohaliste paaritute arvude korrutis, mis on jaguvad juhuslikult genereeritud arvuga.
'''try:
    import random

    for i in range(1, 101):
        if i % 2 == 1:
            ranarv = random.randint(1, 10)
            korrutis = i * ranarv
            print(f'random arv kahekonaliste jagatud {ranarv} võrdub {korrutis:.2f}')
        else:
            print("see on kahekohalised arv")
except:
    print("Sisesta ainult numbreid")'''
    

#12 Heina niitmise brigaadis on N niidukit.
#Esimene niiduk töötas m tundi, iga järgmine 10 minutit rohkem kui eelmine.
#Leia, kui mitu tundi töötas kogu brigaad kokku.
'''try:
    n = int(input("Sisesta niidukite arv N: "))
    m = float(input("Sisesta esimese niiduki tööaeg tundides m: "))
    kokku_aeg = 0
    for i in range(n):
        niiduki_aeg = m + (i * (10 / 60))  # iga järgmine niiduk töötab 10 minutit rohkem
        kokku_aeg += niiduki_aeg
    print(f"Kogu brigaadi tööaeg on {kokku_aeg:.2f} tundi")
except:
    print("Sisesta ainult numbreid")'''
    
#13  Leia kõik naturaalarvud 100-st kuni 1000-ni, mis on 7-ga jaguvad.
# Arvuta ka nende arv ja summa.
'''try:
    summa = 0
    arvude_arv = 0        
    for i in range(100,1001):
        if i % 7==0:
            summa += i
            arvude_arv += 1
            print(i)
            print(f"Arvude summa on {summa}")
            print(f"Arvude arv on {arvude_arv}")
except:
    print("Sisesta ainult numbreid")'''
    
#14 Koosta programm, mis arvutab korrutise arvudest 1 kuni N.
#N väärtus genereeritakse juhuslikult.

'''import random

n = random.randint(1, 100)
print(f"random arv {n}")
arv = 1
for i in range(1, n + 1):
    arv *= i
print(f"Arvude korrutis vahemikus 1 kuni {n} on {arv:.2f}")'''

#15  Kirjuta programm, mis väljastab 10 rida, igal real arvud 0-st kuni 9-ni, näiteks:
#0 1 2 3 4 5 6 7 8 9
#0 1 2 3 4 5 6 7 8 9
#...................
#0 1 2 3 4 5 6 7 8 9

'''for i in range(10):
    for j in range(1, 10):
        print(j, end=' ') # see on et jookseb üksteise järel
        
    print() # see on et läheb järgmisele reale'''
    
#16 Kirjutage programm, mis väljastab veeruna read järgmises vormis:

#1 0 0 0 0 0 0 0 0
#0 2 0 0 0 0 0 0 0
#0 0 3 0 0 0 0 0 0
#0 0 0 4 0 0 0 0 0
#0 0 0 0 5 0 0 0 0
#0 0 0 0 0 6 0 0 0
#0 0 0 0 0 0 7 0 0
#0 0 0 0 0 0 0 8 0
#0 0 0 0 0 0 0 0 9

'''for i in range(1, 10):
    for j in range(1, 10):
        if i == j: # kui i võrdub j-ga
            print(i, end=' ') # kui i võrdub j-ga, siis prindib i
        else:
            print(0, end=' ') # kui i ei võrdu j-ga, siis prindib 0
    print()'''
    
#17 Kirjutage programm, mis väljastab veeruna kasutaja määratud arvu korrutustabeli järgmises vormis:
#2*1=2
#2*2=4
#2*3=6
#2*4=8
#2*5=10
#2*6=12
#2*7=14
#2*8=16
#2*9=18

'''try:
    arv  = int(input("Sisesta arv: "))
    for i in range (1, 11):
        tulemus = arv * i
        print(f"{arv} x {i} = {tulemus}")
except:
    print("Sisesta ainult numbreid")'''
 #18 Antud on naturaalarvud 20-st kuni 50-ni. Väljasta need arvud, mis jaguvad 3-ga, kuid ei jaga 5-ga.
    
'''for i in range(20, 51):
    if i % 3 == 0:
        print(f"{i} on jaguv 3-ga")
    elif i % 5 != 0:
        print(f"{i} on mitte jaguv 5-ga")'''
        
#19 Antud on naturaalarvud 35-st kuni 87-ni. Leia ja väljasta need arvud, mille jagamisel 7-ga jääk on 1, 2 või 5.

'''for i in range(35, 88):
    if i % 7 == 1 or i % 7 == 2 or i % 7 == 5:
        print(f"{i} jagamisel 7-ga jääk on 1, 2 või 5")'''
# 20 Antud on naturaalarvud 1-st kuni 50-ni. Leia nende arvude summa, mis jaguvad 5 või 7-ga. 
'''summa = 1       
for i in range(1, 51):
    if summa % 5 or summa % 7 == 0:
        summa += i
        print(f"Arvude summa on {summa}")'''
#21 Klaviatuurilt sisestatakse 10 arvu – nii positiivseid kui ka negatiivseid.
#Asenda kõik negatiivsed arvud nende absoluutväärtustega ja väljasta saadud 10 arvu.  
      
'''for i in range(1, 11):       
    arv = int(input("Sisesta arv: "))
    if arv < 0:
        arv *= -1
    print(f"Absoluutväärtus on {arv}")'''
  # 22   Leia arvude 100 kuni 200 summa, mis on 17-ga jaguvad.  
'''summa = 1
for i in range(100, 201):
    if i % 17 == 0:
        summa += i
print(f"Arvude summa on {summa}")'''

#23 Arvutisse sisestatakse N punkti koordinaadid.
#Määrata, mitu neist punktidest jääb raadiusega R ringi sisse, mille keskpunkt on punktis (a, b).

'''
    N = int(input("Sisesta punktide arv N: "))
    a = float(input("Sisesta ringi keskpunkti x-koordinaat a: "))
    b = float(input("Sisesta ringi keskpunkti y-koordinaat b: "))
    R = float(input("Sisesta ringi raadius R: "))'''
    
#24  Arvutisse sisestatakse järjest N õpilase pikkused.
# Määrata klasside õpilaste keskmine pikkus.
'''try:
    n = int(input("Sisesta õpilaste arv N: "))
    summa = 0   
    for i in range(n):
        pikkus = float(input(f"Sisesta õpilase {i+1} pikkus: "))
        summa += pikkus
    keskmine = summa / n
    print(f"Õpilaste keskmine pikkus on {keskmine:.2f} cm")
except:
    print("Sisesta ainult numbreid")'''

#25  Antud on naturaalarv N.
#Leia, mitu naturaalarvu, mis ei ületa N, ei jagu ühegagi arvudest 2, 3 või 5.
'''try:
    N = int(input("Sisesta naturaalarv N: "))
    loendur = 0
    for i in range(1, N + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i <= N:
            loendur += 1
    print(f"Naturaalarvud, mis ei ületa {N} ja ei jagu  2, 3 ega 5 on: {loendur}")
except:
    print("Sisesta ainult numbreid")'''
    
#26 Kaks kahekohalist arvu, mis on kirjutatud üksteise järel, moodustavad neljakohalise arvu, mis jagub nende korrutisega.
# Leia need arvud.

'''try:
    arv1 = int(input("Sisesta esimene kahekohaline arv: "))
    arv2 = int(input("Sisesta teine kahekohaline arv: "))
    if 10 <= arv1 <= 99 and 10 <= arv2 <= 99:
        arv = int(f"{arv1}{arv2}")
        print("Neljakohaline arv on:", arv)
        
        if int(arv) % (arv1 * arv2) == 0:
            print(f"Need arvud on {arv1} ja {arv2}")
        else:
            print("Need arvud ei vasta tingimustele.")
except:
    print("Sisesta ainult numbrid")'''
    
#Antud on kaks kahekohalist arvu A ja B.
#Nendest moodustatakse kaks neljakohalist arvu:

#esimene saadakse, kui kirjutatakse esmalt A, seejärel B;

#teine saadakse, kui kirjutatakse esmalt B, seejärel A.
#Leia arvud A ja B, kui on teada, et esimene neljakohaline arv jagub 99-ga,
#ja teine 49-ga.

'''for arv1 in range(10, 100):
    for arv2 in range(10, 100):
        arv_a = int(f"{arv1}{arv2}")
        arv_b = int(f"{arv2}{arv1}")
        print("Neljakohaline arv on:", arv_a, arv_b)
        if int(arv1) % 99 == 0 and int(arv2) % 49 == 0:
            print(f"Need arvud on {arv1} ja {arv2}")'''
            
            
#Loo „mini-loterii” programm.
#Arvuti „mõtleb välja” suvalise arvu, ja kasutaja peab selle ära arvama.
#Lõpuks tuleb kuvada, mitu katset kasutaja tegi.

'''import random
mõeldud_arv = random.randint(1, 10)
katsete_arv = 0
while True:
    kasutaja_arv = int(input("Arva ära arv (1-10): "))
    katsete_arv += 1
    if kasutaja_arv == mõeldud_arv:
        print(f"Õige! Arvasid ära {katsete_arv} katsega.")
        break
    else:
        print("Vale, proovi uuesti.")'''
        
 #Kirjuta programm, mis väljastab veeruna read järgmisel kujul:
#x 0 0 0 0 0 0 0 0
#x x 0 0 0 0 0 0 0
#x 0 x 0 0 0 0 0 0
#x 0 0 x 0 0 0 0 0
#x 0 0 0 x 0 0 0 0
#x 0 0 0 0 x 0 0 0
#x 0 0 0 0 0 x 0 0
#x 0 0 0 0 0 0 x 0
#x 0 0 0 0 0 0 0 x

'''for i in range(1, 10): #read
    for j in range(1, 10): #veerud
        if i == j: # kui i võrdub j-ga
            print('x', end=' ') # kui i võrdub j-ga, siis prindib i
        elif j == 1:
            print('x', end=' ') # kui i võrdub j-ga, siis prindib i
        else:
            print(0, end=' ') # kui i ei võrdu j-ga, siis prindib 0
    print()'''
    
#Programmis luuakse juhuslikku arvu M ja N.
#Ekraanile väljastatakse kahes reas arvujad:
#üks N-st M-ni ja teine ​​​​M-st N-ni.


'''import random

M = random.randint(1, 100)
N = random.randint(1, 100)
print(f"Juhuslik arv M: {M}")
print(f"Juhuslik arv N: {N}")
if M < N:
    print("Arvud N-st M-ni:")
    for i in range(N, M - 1, -1):
        print(i, end=' ')
    print("\nArvud M-st N-ni:")
    for i in range(M, N + 1):
        print(i, end=' ')
else:
    print("Arvud N-st M-ni:")
    for i in range(N, M + 1):
        print(i, end=' ')
    print("\nArvud M-st N-ni:")
    for i in range(M, N - 1, -1):
        print(i, end=' ')'''
        
        
#Spongi Bob praeb kotlette 🍔
#Tal on K kotletti, ja ühele pannile mahub M kotletti.
#Arvuta, mitu täis pannitäit tuleb praadida ja mitu kotletti jääb viimaseks panniks.
try:
    K = int(input("Sisesta kotlettide arv K: "))
    M = int(input("Sisesta pannile mahtuvate kotlettide arv M: "))
    täis_pannitäid = K // M
    jääk_kotletti = K % M
    print(f"Täis pannitäid tuleb praadida: {täis_pannitäid}")
    print(f"Kotletti jääb viimaseks panniks: {jääk_kotletti}")
except:
    print("Sisesta ainult numbreid")
        


            

        


      

    
        
        
        
        
    
    
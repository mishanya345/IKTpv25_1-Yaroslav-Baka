# 1.
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
# from os import PathLike

'''print("Tere maailm!")
nimi = input("sisesta oma nimi: ").capitalize()
print(f"Tere maailm! Tervian sind {nimi}")
vanus = int(input("Sisesta oma vanus: "))# konvertib stringi täis arvuks
print(f"Tere maailm! Tervian sind {nimi.upper()}. Sa oled {vanus} aastat vana")
print(f"Tere maailm! Tervian sind {nimi.lower()}. Sa oled {vanus} aastat vana")'''


# 2

# Mis tüüpi on järgnevad muutujad:

# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.

'''vanus = 18 #int
eesnimi = "Jaak" #str
pikkus = 16.5 #float
kas_käib_koolis = True #bool
print(f"vanus {vanus} on: {type(vanus)}")
print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
print(f"pikkus {pikkus} on: {type(pikkus)}") 
print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")'''


# 3

# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.

'''from random import *
laua_peal = randint(10, 50) #juhuslik arvu 10-50
print(f"Laual on {laua_peal} kommi")
võtab = int(input("Mitu kommi soovid laualt võtta? ")) #sisend võtab teisendab stringi täisarvuks
laua_peal -= võtab #laua_peal = laua_peal - võtab, võtab laualt kommid maha
print(f"Nüüd on laual {laua_peal} kommi")'''


# 4

# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.

''' from math import *

C = int(input("Sisesta puu ümbermõõdu cm: "))
C= C/pi
print(f"Puu ümbermõõt on {C:.2f} cm") # ümardab 2 kohta pärast koma'''

# 5.
# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.

'''from math import * N = int(input("Sisesta maatüki N külje pikkus: "))
M = int(input("Sisesta maatüki M külje pikkus: "))
d = sqrt(N**2 + M**2)
print(f"Maatüki diagonaal on {d:.2f} ühikut")'''

# 6
# Leidke järgnevast näiteprogrammist semantiline viga:
'''aeg = int(input("Mitu tundi kulus sõiduks?: "))
teepikkus = int(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

printf"Sinu kiirus oli {kiirus} km/h")'''

#7.
#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
#Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.

'''num1 = int(input("Sisesta 1. täisarv: "))
num2 = int(input("Sisesta 2. täisarv: "))
num3 = int(input("Sisesta 3. täisarv: "))
num4 = int(input("Sisesta 4. täisarv: "))
num5 = int(input("Sisesta 5. täisarv: "))
summa = num1 + num2 + num3 + num4 + num5
keskmine = summa / 5
print(f"Arvude {num1}, {num2}, {num3}, {num4}, {num5} summa on {summa} ja aritmeetiline keskmine on {keskmine}")'''

#8.
#Joonista samasugune konn
#   @..@
#   (----)
#  ( \__/ )
#  ^^ "" ^^  

'''print("    @..@")
print("   (----)")
print("  ( \\__/ )")
print('  ^^ "" ^^  ')'''

#9.
#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)

'''a = int(input("Sisesta kolmnurga 1. külje pikkus: "))
b = int(input("Sisesta kolmnurga 2. külje pikkus: "))
c = int(input("Sisesta kolmnurga 3. külje pikkus: "))
P = a + b + c
print(f"Kolmnurga ümbermõõt on {P} ühikut")'''

#10
# Pitsa

#Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
#Jätate teenindajale 10% jootraha.
#Koosta programm, mis arvutab, kui palju igaüks peab maksma.

P = int(input("Mitu inimest on? "))
hind = 12.90
jootraha = hind * 0.1
kokku = hind + jootraha
inimese_osa = kokku / P
print(f"Pitsa hind on {kokku:.2f} eurot")
print(f"Iga inimene peab maksma {inimese_osa:.2f} eurot")
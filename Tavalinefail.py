#1
from modulifail import*


'''print("Lahendame/testime 5 arvutehet")
for i in range(5):
    arv1 = float_kontroll(input("sisesta esimene arv: "))
    arv2 = float_kontroll(input("sisesta teine arv: "))
    t = input("sisesta tehe(+,-,*,/):")

    tulemus = arithmetic(arv1, arv2, t)
    print(arv1, arv2, t)
    print(f"{arv1} {t} {arv2} = {tulemus}")'''


#2

'''for i in range(3):
    aasta=int_kontroll(input("Sisesta aasta: "))
    if is_year_leap(aasta):
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} on tavaline aasta")'''


#3
'''
külje_pikkus=float_kontroll(input("Sisesta ruudu külje pikkus: "))
pindala, ümbermõõt, diagonaal=square(külje_pikkus)
print(f"Ruudu pindala on {pindala}, ümbermõõt on {ümbermõõt}, diagonaal on {diagonaal}")'''

#4
'''
kuu=int_kontroll(input("Sisesta kuu number (1-12): "))
kuu=season(kuu)
print(f"on aastaaja {kuu}")'''

#5
'''
arv = int_kontroll(input("Sisesta positiivne täisarv: "))
aasta = int_kontroll(input("Sisesta aasta: "))
arv1 = pangahoius(arv)
print(f"Sisestasid arvu pärast kontrolli: {arv1}")'''

#6

'''aglarv = is_prime(int_kontroll(input("Sisesta positiivne täisarv: ")))
if aglarv:
    print("Sisestatud arv on algarv")
else:
    print("Sisestatud arv ei ole algarv")'''
    
#7 
'''day = int_kontroll(input("Sisesta kuu päev (1-31): "))
month = int_kontroll(input("Sisesta kuu number (1-12): "))
year = int_kontroll(input("Sisesta aasta (nt 2024): "))
print(f"Sisestatud kuupäev: {day}.{month}.{year}")
print(today(day, month, year))'''

#9
ask_kokku = int_kontroll(input("Mitu arvu soovid ostida keskmise arvutamiseks? "))

arvud = []
for i in range(ask_kokku):
    arv = float_kontroll(input(f"Sisesta {i+1}. arv: "))
    arvud.append(arv)
keskmine = average(*arvud)
print(f"Arvude keskmine on: {keskmine}")

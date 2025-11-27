# 1️⃣ Sõna või lause analüüs
# Sisesta sõna või lause.
# Loenda:

# mitu täishäälikut 

# mitu kaashäälikut 

# kui sisestati lause – loenda ka tühikud ja kirjavahemärgid 
'''import string


t =['a','e','i','o','u','õ','ä','ö','ü',]
k = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','š','z','ž','t','v','w','x','y']
m = string.punctuation + string.whitespace

sona=(input("Sisesta sõna või lause analüüsile: ")).lower()
täishäälikud=0
kaashäälikud=0
märgid=0
for i in sona:
    if i in t:
        täishäälikud +=1
    elif i in k:
        kaashäälikud +=1
    elif i in m:
        märgid +=1
print(f"Sõnas või lauses on {täishäälikud} täishäälikut, {kaashäälikud} kaashäälikut ja {märgid} märki.")'''
# 2.1 Nimed 👥
# Küsi kasutajalt viis nime.

# Salvesta nimed loendisse ja kuva need tähestikulises järjekorras.

# Kuva viimane lisatud nimi.

# Lisa võimalus nimekirjas olevaid nimesid muuta ✍️
'''nimed = []
for i in range(5):
    nimi = input("Sisesta nimi: ")
    nimed.append(nimi)
print(nimed)
viimane_nimi = nimed[-1]
nimed.sort()
print("Nimed tähestikulises järjekorras: ", nimed)
print("Viimane lisatud nimi: ", viimane_nimi)

replace = input("Kas soovid mõnda nime muuta? (jah/ei): ").lower()
if replace == 'jah':
    vananimi = input("Sisesta nimi, mida soovid muuta: ")
    uusnimi = input("Sisesta uus nimi: ")
    if vananimi in nimed:
        indeks = nimed.index(vananimi)
        nimed[indeks] = uusnimi
        print("Nimekiri pärast muutmist: ", nimed)
    else:
        print("Nime ei leitud nimekirjast.")'''

  



# 2.2 Kordustega nimed 🔁
# Antud on loend kordustega.
# Koosta programm, mis väljastab nimed ilma kordusteta.

'''nimed = ['Juku', 'Mari', 'Peeter', 'Juku', 'Kati', 'Mari', 'Jüri']
ilma_kordusteta = list(set(nimed))
print(ilma_kordusteta)'''

# Koosta vanuste loend ja leia:

# suurim

# väikseim

# kogusumma

# keskmine

'''vanused = [25, 30, 22, 28, 35, 30, 22]
suurim = max(vanused)
väikseim = min(vanused)
kogusumma = sum(vanused)
keskmine = kogusumma / len(vanused)
print(f"Suurim vanus: {suurim}")
print(f"Väikseim vanus: {väikseim}")
print(f"Kogusumma: {kogusumma}")
print(f"Keskmine vanus: {keskmine:.2f}")'''

#  Tärnide lintdiagramm ⭐
# Kasuta loendis olevaid arve ja joonista tärnidega diagramm.

# ******************
# *******************
# ********************************
# *****************************************
# ****************************************************
# ************
'''list = [18, 19, 32, 41, 52, 12]
for arv in list:
    print('*' * arv)'''
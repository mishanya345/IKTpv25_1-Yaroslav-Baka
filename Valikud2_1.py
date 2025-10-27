'''paev=input("sisesta päeva nimetus =>" )''' # puudu olid jutumärgid
#kui on neljapaev, siis "Uraaa, programeerimine"
'''if paev.lower()=="neljapäev":
    print("Uraaa, programeerimine")'''
    
#kui ei ole neljapaev, siis "Igatsen, programeerida tahaks!"
'''if paev.lower()=="neljapäev":
    print("Uraaa, programeerimine")
else:
    print("Igatsen, programeerida tahaks!")'''

#3 Tööpaevad ja nädalas
'''if paev.lower()=="laupäev" or paev.lower()=="pühapäev":
    print("Lõpuks, pean tööl käima")
else:
    print("Tööpäev, pean tööl käima")'''

# 4 1-esmaspäev, 2-teisipäev, 3-kolmapäev, 4-neljapäev, 5-reede, 6-laupäev, 7-pühapäev
'''paev=int(input("Sisesta päeva number =>(1-7)"))
if paev==1:
    print("Esmaspäev")
elif paev==2:
    print("Teisipäev")
elif paev==3:
    print("Kolmapäev")
elif paev==4:
    print("Neljapäev")
elif paev==5:
    print("Reede")
elif paev==6:
    print("Laupäev")
elif paev==7:
    print("Pühapäev")
else:
    print("Vale number, palun kirjuta 1-7")'''

# isalnum() — Возвращает True, если все символы в строке являются буквенно-цифровыми (буквы или цифры).

# isalpha() — Возвращает True, если все символы в строке — буквы алфавита.

# isascii() — Возвращает True, если все символы в строке являются ASCII-символами.

# isdecimal() — Возвращает True, если все символы в строке — десятичные цифры.

# isdigit() — Возвращает True, если все символы в строке — цифры.

# isidentifier() — Возвращает True, если строка является корректным идентификатором (например, для переменных в Python).

# islower() — Возвращает True, если все символы в строке — строчные буквы.

# isnumeric() — Возвращает True, если все символы в строке — числовые символы (включая цифры и числовые символы других систем).

# isprintable() — Возвращает True, если все символы в строке — печатные (то есть видимые).

# isspace() — Возвращает True, если все символы в строке — пробельные символы (пробелы, табуляция и т.п.).

# istitle() — Возвращает True, если строка оформлена в стиле заголовка (каждое слово начинается с заглавной буквы).

# isupper() — Возвращает True, если все символы в строке — заглавные буквы.

# 1. Juku

# a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.

# b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)

# <6 aastad  - tasuta
# 6-14 - lastepilet
# 15-65 - täispilet
# >65 - sooduspilet
# <0 ja >100 viga andmetega


'''eesnimi = input("Sisesta oma eesnimi => ")
if eesnimi=="JUKU":
    print("Lähme Jukuga kinno")
    vanus = input("Sisesta oma vanus => ")
    if vanus.isdigit():
        vanus = int(vanus)
        if vanus < 0 or vanus > 100:
            print("Viga andmetega")
        elif vanus < 6:
            print("Pilet on tasuta")
        elif vanus <= 14:
            print("Lastepilet")
        elif vanus <= 65:
            print("Täispilet")
        else: 
            print("Sooduspilet")
    else:
        print("Palun sisesta täisarv vanuse kohta")'''

# 2 Pinginaabrid

# Küsi kahe inimese nimed. Kui nimed koosnevad ainult tähedest siis  teavita kasutajat, kas nad on täna pinginaabrid või ei mitte.
'''nimi1 = input("Sisesta nimi => ").capitalize()
nimi2 = input("Sisesta nimi => ").capitalize()
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1=="Yaroslav" and nimi2=="Kirill" or nimi1=="Kirill" and nimi2=="Yaroslav":
        print(f"{nimi1} ja {nimi2} on täna pinginaabrid")
    else:
        print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid")
else:
     print("Palun sisesta ainult tähed")'''

# 3 Remont

# Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind

# Lisaküsimus: kas ta teeb remonti ise või teeb seda professionaali abiga? Kui tegemist on professionaaliga, siis palun arvutage välja, kui palju remont koos tööga maksab.

'''pikkus = int(input("Sisesta toa pikkus => "))
laius = int(input("Sisesta toa laius => "))
if pikkus >0 or laius >0:
    pindala = pikkus * laius
    print(f"pindala suurus on {pindala}")
    user = input("Kas soovid remonti teha? (jah/ei) => ").lower()
    if user.isalpha() and user =="jah":
        hind = float(input("Kui palju maksab ruutmeeter? => "))
        if hind >0:
        
            remont = pindala * hind
            print(f"Remont maksab {remont} eurot")
            Kes = input("Kas teed remonti ise või töötaja? (ise/töötaja) => ").lower()
            if Kes.isalpha() and Kes == "ise":
                print(f"Siis remont maksab {remont} eurot")
            elif Kes.isalpha() and Kes == "töötaja":
                print(f"Siis remont maksab {remont*1.2} eurot")
        else:
            print("hind ei saa ole negatiivne")
    else:
        print("Head aega!")
else:
    print("sisesta positiivne arv")'''

# 4 Allahindus

#  Leia 30% soodustusega hinna, kui alghind on suurem kui 700

'''hind = input("Sisesta toote hind => ")
if hind.isdigit():
    hind = float(hind)
    if hind > 700:
        hind *= 0.7
        print(f"Toote hind on {hind} eurot")
    else:
        print(f"Toote hind on {hind} eurot")
else:
    print("On vaja ainult numbri sisestada")'''

# 5 Temperatuur

# Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)
'''try:
    temp = float(input("Sisesta temperatuur => "))
    if temp > 18:
        print("Ilm on soe")
    else:
        print("Ilm on külm")
except:
    print("KIRJUTA AINULT ARV")'''

# 6 Pikkus

# Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)

'''try:
    pikkus = float(input("Sisesta oma pikkus => "))
    if pikkus < 150:
        print("Oled lühike")
    elif pikkus <= 180:
        print("Oled keskmine")
    else:
        print("Oled pikk")
except:
    print("KIRJUTA AINULT ARV")'''

# 7 Pikkus ja sugu

# Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).

'''try:
    pikkus = float(input("Sisesta oma pikkus => "))
    sugu = input("Sisesta oma sugu (mees või naine)=> ").lower()
    if sugu.isalpha():
        if sugu == "mees":
            if pikkus <= 160:
                print("Oled lühike mees")
            elif pikkus <= 190:
                print("Oled keskmine mees")
            else:
                print("Oled pikk mees")
        elif sugu == "naine":
            if pikkus < 150:
                print("Oled lühike naine")
            elif pikkus <= 180:
                print("Oled keskmine naine")
            else:
                print("Oled pikk naine")
        else:
            print("Palun sisesta mees või naine")
    else:
        print("Palun sisesta ainult tähed")
except:
    print("KIRJUTA AINULT ARV")'''


# 8 Poes

# Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad. Teata, mis summa maksma läheb(Kuva ekraanil tšekk).


'''import random
try:
    piim = random.randint(1,5)
    sai = random.randint(1,5)
    leib = random.randint(1,5)
    print(f"Piim maksab {piim} eurot")
    print(f"Sai maksab {sai} eurot")
    print(f"Leib maksab {leib} eurot")
    summa = 0
    summa_piim = 0
    summa_sai = 0
    summa_leib = 0
    user = input("Kas soovid osta piima? (jah/ei) => ").lower()
    if user.isalpha() and user == "jah":
        kogus = int(input("Mitu tükki soovid osta? => "))
        if kogus > 0:
            summa_piim += piim * kogus
            print(f"Kokku maksad piim {summa_piim} eurot")
        else:
            print("Palun sisesta positiivne arv")

    user = input("Kas soovid osta saia? (jah/ei) => ").lower()
    if user.isalpha() and user == "jah":
        kogus = int(input("Mitu tükki soovid osta? => "))
        if kogus > 0:
            summa_sai += sai * kogus
            print(f"Kokku maksad sai {summa_sai} eurot")
        else:
            print("Palun sisesta positiivne arv")
    
    user = input("Kas soovid osta leiba? (jah/ei) => ").lower()
    if user.isalpha() and user == "jah":
        kogus = int(input("Mitu tükki soovid osta? => "))
        if kogus > 0:
            summa_leib += leib * kogus
            print(f"Kokku maksad leib {summa_leib} eurot")
        else:
            print("Palun sisesta positiivne arv")
    summa = summa_piim + summa_sai + summa_leib
    print(f"Kokku maksad kõik {summa} eurot")
            
except:
    print("KIRJUTA AINULT ARV")'''
    
#9 Ruut

#Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
#Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

'''pikkus = input("Sisesta ruudu külje pikkus => ")
laius = input("Sisesta ruudu külje laius => ")
try:
    pikkus = int(pikkus)
    laius = int(laius)
    if pikkus > 0 and laius > 0:
        if pikkus == laius:
            print("See on ruut")
        else:
            print("See ei ole ruut")
    else:
        print("Palun sisesta positiivne arv")
except:
    print("KIRJUTA AINULT ARV")'''
    
#10 Matemaatika
#Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
#Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

'''try:
    arv1 = float(input("Sisesta esimene arv => "))
    arv2 = float(input("Sisesta teine arv => "))
    tehe = input("Sisesta tehe (+-*/) => ")
    if tehe == "+":
        print(f"{arv1} + {arv2} = {arv1 + arv2}")
    elif tehe == "-":
        print(f"{arv1} - {arv2} = {arv1 - arv2}")
    elif tehe == "*":
        print(f"{arv1} * {arv2} = {arv1 * arv2:.2f}")
    elif tehe == "/":
        if arv2 != 0:
            print(f"{arv1} / {arv2} = {arv1 / arv2:.2f}")
        else:
            print("Nulliga ei saa jagada")
except:
    print("Palun sisesta ainult + - * või /")'''

#11 Juubel
#Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
#Plokkskeemi pole vaja!

'''user = input("Sisesta oma sünnipäev (näiteks:11.12) => ").lower()
if user == "25.11":
    print("Palju õnne, sul on juubel!")
else:
    print("Täna ei ole su juubel!")'''
    
#12 Müük
#Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
#Kuva toote lõplik hind. Plokkskeemi pole vaja!  

'''hind = input("Sisesta toote hind => ")
try:
    hind = float(hind)
    if hind > 0:
        if hind <= 10:
            hind *= 0.9
            print("sinu tegevus on 10%")
            print(f"Toote hind on {hind:.2f} eurot")
        else:
            hind *= 0.8
            print("sinu tegevus on 20%")
            print(f"Toote hind on {hind:.2f} eurot")
    else:
        print("Hind ei saa olla negatiivne")
except:
    print("KIRJUTA AINULT ARV")'''
    
#13 Jalgpalli meeskond
#Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
#Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
#Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita

'''sugu = input("Sisesta oma sugu (mees või naine) => ").lower()
if sugu.isalpha():
    if sugu == "mees":
        vanus = input("Sisesta oma vanus => ")
        if vanus.isdigit():
            vanus = int(vanus)
            if 16 <= vanus <= 18:
                print("Sobid meeskonda")
            else:
                print("Ei sobi meeskonda")
        else:
            print("Palun sisesta täisarv vanuse kohta")
    elif sugu == "naine":
        print("Kahjuks naised ei saa meeskonda kandideerida")
    else:
        print("Palun sisesta mees või naine")'''
        
#14
#Busside logistika

#Olgu meil vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. Mitu bussi on vaja selleks, et kõik inimesed kohale saaksid, ja mitu inimest on viimases bussis (eeldusel, et eelmised on kõik täiesti täis)? Kirjuta programm, mis küsib inimeste arvu ja busside suuruse ning lahendab seejärel selle ülesande.

    
'''try:
    inimesed = int(input("Sisesta inimeste arv => "))
    buss = int(input("Sisesta busside suurus => "))
    if inimesed > 0 and buss > 0:
        busside_arv = inimesed / buss
        busside_arv = int(busside_arv)
        viimases_bussis = inimesed % buss
        if viimases_bussis == 0:
            viimases_bussis = buss
        print(f"Vaja on {busside_arv} bussi")
        print(f"Viimases bussis on {viimases_bussis} inimest")
    else:
        print("Palun sisesta positiivne arv")
except:'''
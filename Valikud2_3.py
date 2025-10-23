print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Mis on su nimi? ").capitalize()
print(f"{nimi}, oi kui ilus nimi!")
try:
    soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
    if soov==1:
        print("Indeksi leidmine")
        while True:
            try:
                mass = float(input("Sisesta oma mass kilogrammides: "))
                if 0 < mass <=200:
                    break
                else:
                    print("Palun sisesta mass õigesti!")
            except:
                  print("Palun sisesta numbrid õigesti!")
        while True:
            try:
                pikkus = float(input("Sisesta oma pikkus meetrites(sm): "))
                if 0 < pikkus <=250:
                    break
                else:
                    print("Palun sisesta pikkus õigesti!")
            except:
                  print("Palun sisesta numbrid õigesti!")

        indeks = mass / (0.01*pikkus ** 2)
        print(f"{nimi}, Sinu keha indeks {indeks:.2f} on:")
        if indeks < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= indeks < 19:
            print("normaalkaalus")
        elif 20 <= indeks <= 25:
            print("Ülekaal")
        elif 26 <= indeks <= 30:
            print("rasvumine")
        elif 31 <= indeks <= 35:
            print("Tugev rasvumine")
        elif 36 <= indeks <= 40:
            print("Väga tugev rasvumine")
        elif indeks > 40:
            print("Tervisele ohtlik rasvumine")
        else:
            print("rasvunud")
        print("Kohtumiseni, {nimi}! Igavesti Sinu, Python!")

    elif soov==0:
        print("Okei, võib-olla järgmine kord!")
    else:
        print("kirjuta ainult 1 või 2")
except:
    print("sisesta sõna")
       
import analüsaatorModule
import os
print(os.getcwd())
failid = os.listdir()
laiendid = set()
for f in failid:
    if '.' in f:
        laiendid.add(f.split('.')[-1])
stat = []        
while True:
    valik = input("Vali tegevus:\n1. Leia projektifailid\n2. Analüüsi faili sisu\n3. Loo raporti kataloog\n4. Leia failid algustähega\n5. Välju\nSisesta valik (1-5): ")
    if valik not in ['1', '2', '3', '4', '5']:
        print("Vigane valik, proovi uuesti.")
    try:
        if valik == '1':
            faililaend = analüsaatorModule.leia_projektifailid()
            stat.append(faililaend)
        elif valik == '2':
            analuus = analüsaatorModule.analuusi_faili_sisu()
            stat.append(analuus)
        elif valik == '3':
            raport = analüsaatorModule.loo_raporti_kataloog()
            stat.append(raport)
        elif valik == '4':
            algustahed = analüsaatorModule.leia_failid_algustahega()
            stat.append(algustahed)
        elif valik == '5':
            print("Väljutamine...")
            break
    
    except:
        print("Ilmnes viga, proovi uuesti.")

if os.path.isfile('statistika.txt'):
    os.remove("statistika.txt")
with open("statistika.txt", 'w', encoding='utf-8') as f:
    for rida in stat:
        f.write(str(rida) + "\n")
print("Statistika on salvestatud faili 'statistika.txt'.")
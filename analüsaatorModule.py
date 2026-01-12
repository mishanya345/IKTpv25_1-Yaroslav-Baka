import os
import glob

def leia_projektifailid():
    fail = input("sisesta faililaiendi ilma punktita: ")
    failid = glob.glob(f'*.{fail}')
    print(f"Leitud failid: {failid}")
    return f"'.'+{fail} failid, {failid}"

def analuusi_faili_sisu():
    while True:
        failitee = input("Sisesta faili tee: ")
        if not os.path.isfile(failitee):
            print("Faili ei leitud, proovi uuesti.")
        else:
            fail = open(failitee, 'r', encoding='utf-8')
            sisu = fail.read()
            sõna = input("Sisesta sõna, mida otsida: ")
            sõna_count = sisu.lower().count(sõna.lower())
            length = len(sisu)
        
            fail.close()
            print(f"Sisu: {sisu}")
            print(f"Sõna '{sõna}' esinemiste arv: {sõna_count}")
            print(f"Faili pikkus: {length} tähemärki")
            break
    return f"{sõna_count}\nFaili pikkus: {length}\nSISU FAILIST:\n {sisu}\n"


def loo_raporti_kataloog():
    while True:
        failitee = input("Sisesta raporti kataloogi tee: ")
        ask = input("Kas soovid lisada või kustutada või otsida kataloogi? (l/k/o)").lower()
        
        if ask == 'l':
            if not os.path.isdir(failitee):
                os.mkdir(failitee)
                return f"Kataloog {failitee} on loodud"
            else:
                print("Kataloog on juba olemas.")
                break

                
        elif ask == 'k':
            if not os.path.isdir(failitee):
                print("Kataloogi ei leitud. Palun proovi uuesti.")  
                os.rmdir(failitee)
                return f"Kataloog {failitee} on kustutatud"
            else:
                try:
                    ask2 = input("Kataloogi ei leitud, kas soovid just kustutada? (jah/ei)")
                    if ask2.lower() == 'jah':
                        os.rmdir(failitee)
                        return f"Kataloog {failitee} on kustutatud"
                    elif ask2.lower() == 'ei':
                        print("Kataloogi kustutamine katkestatud.")
                        break
                except:
                    print("palun kirjuta jah või ei")
                    break
                
        elif ask == 'o':
            if not os.path.isdir(failitee):
                print("Kataloogi ei leitud.")
            else:
                print(f"Kataloog {failitee} on leitud.")
                break
      
    return f"{failitee} on leitud"

def leia_failid_algustahega():

    while True:
        algustaht = input("Sisesta algustäht: ")
        if not algustaht.isalpha() or len(algustaht) != 1:
            print("Palun sisesta üks täht.")
        else:
            break
    failid = glob.glob(f'{algustaht}*')
    print(f"Leitud failid: {failid}")
    return f"algustäht failid {algustaht}:\nFailid: {failid}\n Kui palju: {len(failid)}"





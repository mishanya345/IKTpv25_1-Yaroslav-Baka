import os
import glob

def leia_projektifailid():
    fail = input("sisesta faililaiendi ilma punktita: ")
    failid = glob.glob(f'*.{fail}')
    print(f"Leitud failid: {failid}")
    return failid

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
        
            fail.close()
            print(f"Sisu: {sisu}")
            print(f"Sõna '{sõna}' esinemiste arv: {sõna_count}")
            break
    return sisu


def loo_raporti_kataloog():
    while True:
        failitee = input("Sisesta raporti kataloogi tee: ")
        if not os.path.isdir(failitee):
            ask = input("Kataloogi ei leitud, proovi uuesti. Kas soovid lisada kataloogi? (jah/ei)")
            if ask.lower() == 'jah':
                os.mkdir(failitee)
                print("Kataloog on lisatud.")
            else:
                print("Proovi uuesti.")
        else:
            print("Kataloog leitud. ")
            break
    return failitee

def leia_failid_algustahega():
    algustaht = input("Sisesta algustäht: ")
    while True:
        if not algustaht.isalpha() or len(algustaht) != 1:
            print("Palun sisesta üks täht.")
        else:
            break
    failid = glob.glob(f'{algustaht}*')
    print(f"Leitud failid: {failid}")
    return failid





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
            fail.close()
            print(f"Sisu: {sisu}")
            break
    return sisu


def loo_raporti_kataloog():
    while True:
        failitee = input("Sisesta : ")
        if not os.path.isfile(failitee):
            ask = input("Faili ei leitud, proovi uuesti. Kas te tehete lisada faili? (jah/ei)")
            if ask.lower() == 'jah':
                os.mkdir().failitee
                print("Faili on lisatud.")
            else:
                continue
        else:
            print("Fail leitud. ")
            break
    return failitee






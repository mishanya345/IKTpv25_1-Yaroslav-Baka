import os
import glob

def leia_projektifailid():
    """Otsib projektikaustast faile antud laiendiga."""
    fail = input("sisesta faililaiendi ilma punktita: ")
    failid = glob.glob(f'*.{fail}')
    print(f"Leitud failid: {failid}")
    return f".{fail} failid: {failid}"

def analuusi_faili_sisu():
    """
    Analüüsib faili sisu ja otsib antud sõna.
    """
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
    """
    Loob raporti katalooge. See funktioon võimaldab kasutajal lisada, kustutada või otsida katalooge.
    """
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
                    ask2 = input("Kas soovid just kustutada? (jah/ei)")
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
    """
    Otsib projektikaustast faile, mille nimi algab antud tähega.
    """
    while True:
        algustaht = input("Sisesta algustäht: ")
        if not algustaht.isalpha() or len(algustaht) != 1:
            print("Palun sisesta üks täht.")
        else:
            break
    failid = glob.glob(f'{algustaht}*')
    print(f"Leitud failid: {failid}")
    return f"algustäht failid {algustaht}:\nFailid: {failid}\n Kui palju: {len(failid)}"

def loo_raporti_faili():
    """
    Loob raporti faili. See funktioon võimaldab kasutajal lisada, kustutada või otsida faile nagu katalooge funktsioone.
    """
    while True:
        failitee = input("Sisesta raporti faili tee: ")
        ask = input("Kas soovid lisada(l) või kustutada(k) või otsida(o) Faili? (l/k/o): ").lower()
        
        if ask == 'l':
            if not os.path.isfile(failitee):
                fail = open(failitee, 'w', encoding='utf-8')
                fail.close()
                return f"Kataloog {failitee} on loodud"
            else:
                print("Kataloog on juba olemas.")
                break

        elif ask == 'k':
                if not  os.path.isfile(failitee):
                    print("Faili ei leitud. Palun proovi uuesti.") 
                else:
                    try:
                        ask2 = input("Kas soovid just kustutada? (jah/ei)")
                        if ask2.lower() == 'jah':
                            os.unlink(failitee)
                            return f"Faili {failitee} on kustutatud"
                        elif ask2.lower() == 'ei':
                            print("Faili kustutamine katkestatud.")
                            break
                    except:
                        print("palun kirjuta jah või ei")
                        break
                    
        elif ask == 'o':
            for juur, kaustad, failid, in os.walk('.'):
                if failitee in failid:
                    
                    print(f"Faili asukoht: {os.path.join(juur, failitee)}")
                    return f"{os.path.abspath(os.path.join(juur, failitee))} on leitud" #abspath annab kogu tee
                else:
                    print("Faili ei leitud.")
                    break
            break
import analüsaatorModule

while True:
    try:
        faililaend = analüsaatorModule.leia_projektifailid()
        analuus = analüsaatorModule.analuusi_faili_sisu()
        raport = analüsaatorModule.loo_raporti_kataloog()
        break
    except:
        print("Ilmnes viga, proovi uuesti.")
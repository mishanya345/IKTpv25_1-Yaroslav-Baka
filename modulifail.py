#1 töö 5.1
# ül. 1

def arithmetic(a: float, b: float,tehe: str)->any:
    """Lihtne kalkulaator:
    +- liitmine
    -- lahutamine
    */ korrutamine
    /-jagamine
    kul juhul tagastab "tundmatu tehe"
    :param float a: esimene arv
    :param float b: teine arv 
    :param str tehe: tehe, mis tuleb teha
    :return/rtype: tehte tulemus float või str"""
    if tehe in ["+","-","*","/"]:
        if tehe == "/" and b==0:
            vastus= "nulliga jagamine pole lubatud"
        else:
            vastus=eval(f"{a}{tehe}{b}")
    else:
        vastus="Tundmatu tehe"
    return vastus

def float_kontroll(sisend:str)->float:
    """Kontrollib, kas sisestatud andmed on teisendavad float arvuks 
    : param str sisend: kasutaja sisestatud andmed
    : return/rtype: teisendatud float arv """
    while True:
        try:
            arv1 = float(input("sisesta esimene arv: "))
            break
        except: 
            print("palun sisesta arv!")
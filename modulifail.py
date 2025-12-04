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
            arv = float(sisend)
            return arv
        except:
            sisend = input("palun sisesta ainult arv!")


def int_kontroll(sisend:str)->int:
    """Kontrollib, kas sisestatud andmed on teisendavad int arvuks 
    : param str sisend: kasutaja sisestatud andmed
    : return/rtype: teisendatud int arv """
    while True:
        try:
            return int(sisend)
        except:
            print("palun sisesta täisarv:  ")
        break
# ül. 2
def is_year_leap(aasta: int) -> bool:
    """Kontrollib, kas aasta on liigaasta
    :param int aasta: aasta arvuna
    :return/rtype: True kui liigaasta, False kui tavaline aasta"""

    if (aasta % 4 == 0 and aasta % 100 != 0):
        return True
    else:
        return False
    
#ül. 3
def square(külg: float) -> any:
    """Arvutab ruudu pindala, ümbermõõdu ja diagonaali
    :param float külg: ruudu külje pikkus
    :return/rtype: tuple (pindala, ümbermõõt, diagonaal)"""
    pindala = külg ** 2
    ümbermõõt = 4 * külg
    diagonaal = round((külg * 2 ** 0.5), 2)
    return (pindala, ümbermõõt, diagonaal)

#ül. 4
def season(kuu: int) -> str:
    """Määrab kuu põhjal aastaaja
    :param int kuu: kuu arvuna (1-12)
    :return/rtype: str aastaaja nimetus"""
    if kuu in [12, 1, 2]:
        return "talv"
    elif kuu in [3, 4, 5]:
        return "kevad"
    elif kuu in [6, 7, 8]:
        return "suvi"
    elif kuu in [9, 10, 11]:
        return "sügis"
    else:
        return "vigane kuu"
    
def pangahoius(a:float, years:int) -> float:
    """Arvutab pangahoiuse lõppsumma koos intressidega
    :param float a: algne hoiusesumma
    :param int years: aastate arv
    :return/rtype: float lõppsumma"""
    for i in range(years):
        a = a * 1.1
    return round(a, 2)
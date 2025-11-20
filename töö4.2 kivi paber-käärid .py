# Mäng kivi paber käärid
import msvcrt
import random

valikud = ["kivi\r", "paber\r", "käärid\r"]
while True:
    try:

        user1 = input('mis on sinu nimi mängija 1? ')
        user2 = input('mis on sinu nimi mängija 2? ')
        break
    except:
        print("Palun sisesta koreekntne nimi .")
print('kivi... käärid... paber... üks... kaks... kolm')
while True:
        user1 = ''
        print('Mängija 1 vali kivi, paber või käärid: ', end='')
        while True:
            t = msvcrt.getch().decode('utf-8')
            print(t.replace(t, '*'), end='', flush=True)
            user1 += t
            if t =='\r':
                break
        print()
        print(user1)
        if user1 in valikud:
            break
        else:

            print("Palun vali kivi, paber või käärid.")
while True: 
     
        user2 = input("Mängija 2 vali kivi, paber või käärid: ").lower()
        if user2 in valikud:
            break
        else:
            print("Palun vali kivi, paber või käärid.")
while True:
    if user1 == user2:
        print("mitte keegi!")
        break
    elif (user1 == "kivi" and user2 == "käärid") or (user1 == "paber" and user2 == "kivi") or (user1 == "käärid" and user2 == "paber"):
        print("Mängija 1 võidab!")
        break
    elif (user2 == "kivi" and user1 == "käärid") or (user2 == "paber" and user1 == "kivi") or (user2 == "käärid" and user1 == "paber"):
        print("Mängija 2 võidab!")
        break



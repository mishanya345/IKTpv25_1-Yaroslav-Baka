# Mäng kivi paber käärid
import random
valikud = ["kivi", "paber", "käärid"]
user1 = input('mis on sinu nimi mängija 1? ')
user2 = input('mis on sinu nimi mängija 2? ')
print('kivi... käärid... paber... üks... kaks... kolm')
game = True
while game:
    try:
        user1 = input("Mängija 1 vali kivi, paber või käärid: ").lower()
        user2 = input("Mängija 2 vali kivi, paber või käärid: ").lower()
        if user1 in valikud and user2 in valikud:
            break
    except:
        print("Palun vali kivi, paber või käärid.")
while game:
    if user1 == user2:
        print("mitte keegi!")
    elif (user1 == "kivi" and user2 == "käärid") or (user1 == "paber" and user2 == "kivi") or (user1 == "käärid" and user2 == "paber"):
        print("Mängija 1 võidab!")
        game = False
    elif (user2 == "kivi" and user1 == "käärid") or (user2 == "paber" and user1 == "kivi") or (user2 == "käärid" and user1 == "paber"):
        print("Mängija 2 võidab!")
        game = False
küsimus = input("Kas soovite uuesti mängida? (jah/ei): ").lower()
if küsimus != "jah":
    game = False
    print("Aitäh mängimast!")




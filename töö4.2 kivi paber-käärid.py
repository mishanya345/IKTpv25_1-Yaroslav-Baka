# Mäng kivi paber käärid
import msvcrt
print('Tere tulemast mängu kivi, paber, käärid!')
valikud = ["kivi\r", "paber\r", "kaarid\r"]
game = True
while game:
    name1 = input('mis on sinu nimi mängija 1? ')
    name2 = input('mis on sinu nimi mängija 2? ')
  

    print('kivi... käärid... paber... üks... kaks... kolm "puuduta ENTER"')
    while True:
        try:
            user1 = ''
            print('Mängija 1 vali kivi, paber või kaarid: ', end='')
            while True:
                t = msvcrt.getch().decode('utf-8')
                print(t.replace(t, '*'), end='', flush=True)
                user1 += t
                if t =='\r':
                    break
            if user1 in valikud:
                print()
                break
        
            else:
                print()
                print("Palun vali kivi, paber või kaarid.")
        except:
            print()
            print("vabandust eesti tähed ei tööta vöi sa kirjutasin teise sümbolid")

    while True: 
         try:
            user2 = ''
            print('Mängija 2 vali kivi, paber või kaarid: ', end='')
            while True:
                t = msvcrt.getch().decode('utf-8')
                print(t.replace(t, '*'), end='', flush=True)
                user2 += t
                if t =='\r':
                    break
            if user2 in valikud:
                print()
                print(f'Mängija 1 {name1} valisib: {user1}')
                print(f'Mängija 2 {name2} valisib: {user2}')
                break
            else:
                print()
                print("Palun vali kivi, paber või käärid.")

         except:
            print()
            print("vabandust eesti tähed ei tööta vöi sa kirjutasin teise sümbolid")
    while True:
        if (user1 == "kivi\r" and user2 == "kaarid\r") or (user1 == "paber\r" and user2 == "kivi\r") or (user1 == "kaarid\r" and user2 == "paber\r"):
            print()
            print(f"Mängija 1 {name1} võidab!")
            break
        elif (user2 == "kivi\r" and user1 == "kaarid\r") or (user2 == "paber\r" and user1 == "kivi\r") or (user2 == "kaarid\r" and user1 == "paber\r"):
            print()
            print(f"Mängija 2 {name2} võidab!")
            break
        elif user1 == user2:
            print()
            print("mitte keegi!")
            break
    while True:
        veel = input('kas soovite mängida uuesti(jah/ei) ').lower()
        if veel == 'jah':
            break
        elif veel == 'ei':
            print('aitäh mängimast!')
            game = False
            break
        else:
            print('palun vastake jah või ei')




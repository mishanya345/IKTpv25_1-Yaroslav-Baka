#list
#loome listi

from itertools import count


l=[]
print(f'listi tüüp on {l}')
while True:
    print("tee valik:\n1. lisa elemente\n2. lisa elemente pos-le\n3. Eemalda elemente pos järgi\n4. eemade elemen nime järgi\n5. sorteerida elementid\n6. reverseda elemtid \n7. clear kõik \n8.  teise listi elementid lõppu")
    while True:
        try:
            valik=int(input())
            break
        except:
            print('arvnud:1...n')
    print('töö listiga')
    if valik==1:
        while True:
            try:
                i=int(input('mitu elementi soovid listi lisada? '))
                if i>0:
                    break
                else:
                    print('palun sisesta arvnud suurem 0!')
            except:
                print('palun sisesta arvnud !')
               
        for e in range(i):
            element=input(f'sisesta {e}. element: ')
            l.append(element)
        print(f'sinu list on nüüd: {l}')
    elif valik==2:
        while True:
            try:
                pos=int(input(f'sisesta positsioon kuhu soovid lisada : '))
                if 0<=pos<=len(l):
                    break
                else:
                    print(f'palun sisesta arvnud vahemikus 0-{len(l)}')
            except:
                print('palun sisesta arvnud!')
        element=input(f'sisesta element: ')
        l.insert(pos,element)
        print(f'sinu list on nüüd: {l}')
    elif valik==3:
         while True:
            try:
                pos=int(input(f'sisesta positsioon kust soovid eemaldada (0-{len(l)-1}): '))
                if 0<=pos<=len(l)-1:
                    break
                else:
                    print(f'palun sisesta arvnud vahemikus 0-{len(l)-1}')
            except:
                print('palun sisesta arvnud!')
         eem_element=l.pop(pos)
         print('eemaldanud element on:', eem_element)
         print(f'sinu list on nüüd: {l}, eemaldasid elemendi: {eem_element}')

    elif valik==4:

        element=input('sisesta element mida soovid eemaldada: ')
        mitu=l.count(element)
        if mitu==0:
            print('elementi ei leitud listist!')
            break
        else:
            for i in range(mitu):
                print(f'eemaldan {element}. korda elementi: {l.index(element)}')
                l.remove(element)
                
        print(f'eemaldasid {mitu} korda elementi: {element}')
        

        #loend.extend()
        #loend.sort()
        #loend.reverse()
        #loend.clear()
    elif valik==5:
        l.sort()
        print(f'sinu list on nüüd: {l}')


    elif valik==6:
        l.reverse()
        print(f'sinu list on nüüd: {l}')

    elif valik==7:
        l.clear()
        print(f'sinu list on nüüd: {l}')

    elif valik==8:
        teine_list=[]
        while True:
            try:
                i=int(input('mitu elementi soovid teise listi lisada? '))
                if i>0:
                    break
                else:
                    print('palun sisesta arvnud suurem 0!')
            except:
                print('palun sisesta arvnud !')
               
        for e in range(i):
            element=input(f'sisesta {e}. element: ')
            teine_list.append(element)
        l.extend(teine_list)
        print(f'sinu list on nüüd: {l}')
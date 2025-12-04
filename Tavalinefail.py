from modulifail import*

print("Lahendame/testime 5 arvutehet")
for i in range(5):

    arv1 = float_kontroll(input("sisesta esimene arv: "))
    arv2 = float_kontroll(input("sisesta esimene arv: "))

t=input("sisesta tehe(+,-,*,/):")
tulemus=arithmetic(arv1,arv2,t)
print(arv1,arv2,t)
print(f"{arv1} {t} {arv2} = {tulemus}")


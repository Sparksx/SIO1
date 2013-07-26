code = input("Entrez le code du billet")
first = 0
if code[0] == "D":
    first = 4
elif code[0] == "E":
    first = 5
elif code[0] == "F":
    first = 6
elif code[0] == "V":
    first = 22

if first != 0:
    somme = first
    for i in range (1, 12):
        somme = somme + int(code[i])

    if somme % 9 == 8:
        print("Le billet est probablement un vrai")
    else:
        print("Le billet est faux")
else:
    print("Le billet est faux")

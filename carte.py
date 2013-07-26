code = input("Entrez le code de la carte")
somme = 0
for i in range (0, 16):
    temp = int(code[i])
    if i % 2 == 0:
        temp = int(code[i]) * 2
    if temp > 9:
        temp = temp - 9
    somme = somme + temp
if somme % 10 == 0:
    print("le code est valide")
else:
    print("code non valide")

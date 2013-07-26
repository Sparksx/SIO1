from tri import *



i = int(input("Entrez la taille du tableau souhaité"))
n = 0
tab = []

while n < i :
    s = int(input("Entrez la valeur n°" + str(n + 1)))
    tab = tab + [s]
    n += 1

print(tri(tab))

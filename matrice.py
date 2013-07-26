mat = []
lo = int(input("Entez le nombre de lignes de la matrice"))
la = int(input("Entez le nombre de collonnes de la matrice"))


for p in range(lo):
    tab = []
    for q in range(la):
        tab = tab + [0]
    mat = mat + [tab]

for k in range(len(mat)):
    print(mat[k])

mat = []
mat1 = []
lo = int(input("Entez le nombre de lignes de la matrice"))
la = int(input("Entez le nombre de collonnes de la matrice"))


for p in range(lo):
    tab = []
    for q in range(la):
        tab = tab + [6]
    mat = mat + [tab]

for p in range(lo):
    tab = []
    for q in range(la):
        tab = tab + [9]
    mat1 = mat1 + [tab]

for p in range(lo):
    for q in range(la):
        mat[p][q] = mat[p][q] + mat1[p][q]


for k in range(len(mat)):
    print(mat[k])

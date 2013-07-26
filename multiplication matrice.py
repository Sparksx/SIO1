mat = [[1,2,3],[4,5,6]]
mat1 = [[1,2],[3,4],[5,6]]

res = []

for p in range(len(mat)):
    tab = []
    for q in range(len(mat1[0])):
        tab = tab + [0]
    res = res + [tab]

for a in range(len(mat)):
    for b in range(len(mat[0])):
        for c in range(len(mat1[0])):
            for d in range(len(mat1)):
                res[a][c] = mat[a][b] * mat1[d][c]
                print(mat1[d][c])

for k in range(len(res)):
    print(res[k])

mat = [[1,2,3,8,4,3,2],[4,5,6,9,5,6,7]]
li = []
for i in range(len(mat[0])):
    li = li + [0]
mat = mat + [li]

j = 0
for j in range(len(mat)):
    mat[j] = mat[j] + [0]

t = 0
for t in range(len(mat)):
    print(mat[t])

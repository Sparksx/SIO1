p1 = ""
p2 = ""
cose = ""
i = 0
j = 0

p1 = input("Saisisser une phrase a coder")
p1 = p1.upper()
code = input("Saisisser une phrase a coder")
code = code.upper()

while i < len(p1) :
    p2 = p2 + p1[i] + code[j]
    i = i + 1
    if j < (len(code) - 1) :
        j = j + 1
    else :
        j = 0

print(p2)

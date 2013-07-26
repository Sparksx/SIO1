p1 = ""
p2 = ""
i = 0

p1 = input("Saisisser une phrase a coder")
p1 = p1.upper()

while i < len(p1) :
    p2 = p2 + p1[i] + "*"
    i = i + 1

print(p2)

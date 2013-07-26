rang = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
position = 0
phraseCodee = ""

phraseACoder = input("Saisissez une phrase a coder")
phraseACoder = phraseACoder.upper()

rang = int(input("Saisissez la clé de codage"))
rang = rang % 26
    

for lettre in phraseACoder :
    if lettre == " " :
        phraseCodee += " "
    else :
        position = alphabet.find(lettre)
        if position + rang > 25 :
            phraseCodee += alphabet[(position + rang - 26)]
        else :
            phraseCodee += alphabet[(alphabet.find(lettre)+rang)]

print(phraseCodee)

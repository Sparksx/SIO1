rang = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
position = 0
phraseCodee = ""

phraseACoder = input("Saisissez une phrase a decoder")
phraseACoder = phraseACoder.upper()

rang = int(input("Saisissez la clé de codage"))
rang = rang % 26
    

for lettre in phraseACoder :
    if lettre == " " :
        phraseCodee += " "
    else :
        position = alphabet.find(lettre)
        if position - rang < 0:
            phraseCodee += alphabet[(26 + (position -rang))]
        else :
            phraseCodee += alphabet[(position - rang)]

print(phraseCodee)


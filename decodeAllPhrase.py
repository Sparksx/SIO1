rang = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
position = 0
phraseCodee = ""

phraseACoder = input("Saisissez une phrase a decoder")
phraseACoder = phraseACoder.upper()


while rang < 26 :
    phraseCodee = ""
    for lettre in phraseACoder :
        if lettre == " " :
            phraseCodee += " "
        else :
            position = alphabet.find(lettre)
            if position - rang < 0:
                phraseCodee += alphabet[(26 + (position -rang))]
            else :
                phraseCodee += alphabet[(position - rang)]
    rang += 1

    print(phraseCodee)



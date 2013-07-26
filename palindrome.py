phrase = input("Entrez une phrase en minuscule et sans accent")
phrase = phrase.replace(" ", "")
phrase = phrase.lower()

i = 0
size = len(phrase)
palin = True
while i < int(size / 2):
    if phrase[i] != phrase[((size - 1) - i)]:
        palin = False
    
if palin:
    print("c'est un palin")
else:
    print("c'est pas un palin")


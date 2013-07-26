def tri(liste):
    for i in range(0, len(liste) - 1):
        for j in range(0, len(liste) - 1):
            if liste[i] > liste[i + 1]:
                tp = liste[i]
                liste[i] = liste[i + 1]
                liste[i + 1] = tp
    return liste

def triDesc(liste):
    for i in range(0, len(liste) - 1):
        for j in range(0, len(liste) - 1):
            if liste[i] < liste[i + 1]:
                tp = liste[i]
                liste[i] = liste[i + 1]
                liste[i + 1] = tp
    return liste

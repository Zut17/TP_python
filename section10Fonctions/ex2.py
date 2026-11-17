def mention(note, seuil_passable=10, seuil_bien=14):
    if note < seuil_passable:
        return "AJOURNÉ"
    elif note >= seuil_bien:
        return "BIEN"
    return "PASSABLE"

for n in [8, 12, 15]:
    print(n, mention(n))
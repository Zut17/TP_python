notes = [8, 12, 15, 17, 10, 6]
compteur = 0
for note in notes:
    if note >= 10:
        compteur += 1
print(compteur, "notes >= 10")
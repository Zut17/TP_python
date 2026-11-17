## refactorisation de sect05 ex2 selon le principe DRY
def classer(note):
    if note < 10:
        return "ÉCHEC"
    elif note >= 14:
        return "MENTION"
    return "PASSABLE"

for note in [8, 12, 15, 17, 10, 6]:
    print(note, classer(note))
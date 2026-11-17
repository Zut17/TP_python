etudiants = [
    ["Amina", 19, 14.5],
    ["Brice", 21, 12.0],
    ["Chloé", 20, 16.5],
]
print("2e étudiant :", etudiants[1][0])
moyenne_generale = (etudiants[0][2] + etudiants[1][2] + etudiants[2][2]) / 3
print(f"Moyenne générale : {moyenne_generale:.2f}")
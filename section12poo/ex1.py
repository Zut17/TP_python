class Etudiant:
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return self.note_cc * 0.4 + self.note_examen * 0.6


if __name__ == "__main__":
    print(Etudiant("Amina", 12.0, 15.5).moyenne())  # 14.1
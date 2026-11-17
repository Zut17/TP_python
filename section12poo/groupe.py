from etudiant import Etudiant


class Groupe:
    def __init__(self):
        self.etudiants = []

    def ajouter(self, etudiant):
        self.etudiants.append(etudiant)

    def moyenne_generale(self):
        total = 0
        for e in self.etudiants:
            total += e.moyenne()
        return total / len(self.etudiants)


if __name__ == "__main__":
    g = Groupe()
    g.ajouter(Etudiant("Amina", 12.0, 15.5))
    g.ajouter(Etudiant("Brice", 10.0, 11.0))
    print(f"{g.moyenne_generale():.2f}")
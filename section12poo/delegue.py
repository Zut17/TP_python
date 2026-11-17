from etudiant import Etudiant


class Delegue(Etudiant):
    def __init__(self, nom, note_cc, note_examen, filiere):
        super().__init__(nom, note_cc, note_examen)
        self.filiere = filiere

    def presenter(self):
        return f"Je suis {self.nom}, délégué(e) de la filière {self.filiere}."


if __name__ == "__main__":
    d = Delegue("Chloé", 14.0, 16.0, "Génie Logiciel")
    print(d.presenter())
    print(d.moyenne())
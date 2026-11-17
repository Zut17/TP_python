class Etudiant:
    def __init__(self, nom: str):
        self.nom = nom
        self.__notes = []

    def ajouter_note(self, note: float) -> None:
        if not 0 <= note <= 20:
            raise ValueError("La note doit être comprise entre 0 et 20")
        self.__notes.append(note)

    @property
    def moyenne(self) -> float:
        if not self.__notes:
            return 0.0
        return sum(self.__notes) / len(self.__notes)


if __name__ == "__main__":
    e = Etudiant("Amina")
    e.ajouter_note(14)
    e.ajouter_note(16.5)
    print(f"Moyenne : {e.moyenne:.2f}")

    try:
        e.ajouter_note(25)
    except ValueError as err:
        print("Erreur :", err)

    try:
        e.moyenne = 15
    except AttributeError as err:
        print("Erreur :", err)
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nom: str):
        self.nom = nom

    @abstractmethod
    def crier(self) -> str:
        """Retourne le cri de l'animal."""

    def se_presenter(self) -> None:
        print(f"Je m'appelle {self.nom} et je fais : {self.crier()}")


class Chien(Animal):
    def crier(self) -> str:
        return "Wouf !"


class Chat(Animal):
    def crier(self) -> str:
        return "Miaou !"


if __name__ == "__main__":
    for animal in [Chien("Rex"), Chat("Félix")]:
        animal.se_presenter()

    # Décommente pour voir l'erreur :
    # Animal("test")
from typing import Protocol


class Comparable(Protocol):
    def comparer(self, autre) -> int:
        """Retourne un nombre négatif, 0 ou positif."""
        ...


class Note:
    def __init__(self, valeur: float):
        self.valeur = valeur

    def comparer(self, autre) -> int:
        return (self.valeur > autre.valeur) - (self.valeur < autre.valeur)


class Mot:
    def __init__(self, texte: str):
        self.texte = texte

    def comparer(self, autre) -> int:
        return len(self.texte) - len(autre.texte)


def plus_grand(a: Comparable, b: Comparable) -> Comparable:
    return a if a.comparer(b) >= 0 else b


if __name__ == "__main__":
    print(plus_grand(Note(12.5), Note(15)).valeur)
    print(plus_grand(Mot("python"), Mot("abc")).texte)
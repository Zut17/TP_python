import json
import os
from abc import ABC, abstractmethod


class Stockage(ABC):
    @abstractmethod
    def sauvegarder(self, cle: str, valeur) -> None: ...

    @abstractmethod
    def charger(self, cle: str): ...


class StockageMemoire(Stockage):
    def __init__(self):
        self._donnees = {}

    def sauvegarder(self, cle: str, valeur) -> None:
        self._donnees[cle] = valeur

    def charger(self, cle: str):
        return self._donnees.get(cle)


class StockageFichier(Stockage):
    def __init__(self, chemin: str = "donnees.json"):
        self._chemin = chemin

    def _lire(self) -> dict:
        if not os.path.exists(self._chemin):
            return {}
        with open(self._chemin, "r", encoding="utf-8") as f:
            return json.load(f)

    def sauvegarder(self, cle: str, valeur) -> None:
        donnees = self._lire()
        donnees[cle] = valeur
        with open(self._chemin, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)

    def charger(self, cle: str):
        return self._lire().get(cle)


if __name__ == "__main__":
    for stockage in [StockageMemoire(), StockageFichier("test_stockage.json")]:
        stockage.sauvegarder("nom", "Amina")
        stockage.sauvegarder("note", 14.5)
        print(type(stockage).__name__, "->", stockage.charger("nom"), stockage.charger("note"))
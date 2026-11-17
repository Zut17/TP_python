from abc import ABC, abstractmethod


class Payable(ABC):
    @abstractmethod
    def payer(self) -> bool: ...

    @abstractmethod
    def rembourser(self) -> bool: ...


class Paiement(ABC):
    def __init__(self, montant: float):
        self._montant = montant

    @abstractmethod
    def valider(self) -> bool: ...

    def traiter(self) -> str:
        if not self.valider():
            return "Paiement refusé"
        return f"Paiement de {self._montant} FCFA accepté"


class MobileMoney(Paiement, Payable):
    def __init__(self, montant: float, numero: str):
        super().__init__(montant)
        self.__numero = numero

    def valider(self) -> bool:
        return len(self.__numero) == 9 and self._montant > 0

    def payer(self) -> bool:
        print(f"Mobile Money : {self._montant} FCFA débités")
        return True

    def rembourser(self) -> bool:
        print(f"Mobile Money : {self._montant} FCFA remboursés")
        return True


class CarteBancaire(Paiement, Payable):
    def __init__(self, montant: float, numero_carte: str):
        super().__init__(montant)
        self.__numero_carte = numero_carte

    def valider(self) -> bool:
        return len(self.__numero_carte) == 16 and self._montant > 0

    def payer(self) -> bool:
        print(f"Carte : {self._montant} FCFA débités")
        return True

    def rembourser(self) -> bool:
        print(f"Carte : {self._montant} FCFA remboursés sous 5 jours")
        return True


class CashLivraison(Paiement, Payable):
    def valider(self) -> bool:
        return self._montant > 0

    def payer(self) -> bool:
        print(f"Cash : {self._montant} FCFA à encaisser à la livraison")
        return True

    def rembourser(self) -> bool:
        print("Cash : remboursement impossible automatiquement")
        return False


if __name__ == "__main__":
    moyens = [
        MobileMoney(5000, "677123456"),
        CarteBancaire(12000, "1234567812345678"),
        CashLivraison(8000),
    ]
    for m in moyens:
        print(m.traiter())
        m.payer()
        m.rembourser()
        print("---")
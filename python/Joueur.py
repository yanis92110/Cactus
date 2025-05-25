from Paquet import Paquet
from Carte import Carte
class Joueur():
    def __init__(self, paquet: Paquet, etiquette=""):
        super().__init__()
        self.cartes: list = []
        self.etiquette: str = etiquette
        self.score: int = 0
        for i in range(0, 4):
            carte = paquet.pop_carte()
            self.cartes.append(carte)

    def __str__(self):
        return f"Main de {self.etiquette}"

    def getCarte(self, index: int):
        return self.cartes[index]

    def setCarte(self, index: int, carte: Carte):
        self.cartes[index] = carte

    def ajouterCarte(self, carte: Carte):
        self.cartes.append(carte)

    def retirerCarte(self, index: int):
        return self.cartes.pop(index)

    def nombreCartes(self):
        return len(self.cartes)

    def montrerCarte(self, index: int):
        print(self.cartes[index])
    def addScore(self,valeur: int):
        self.score+=valeur

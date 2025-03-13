import Paquet
class MainJoueur():
    def __init__(self, paquet: Paquet, etiquette=''):
        super().__init__()
        self.cartes=[]
        self.etiquette=etiquette
        for i in range(0,4):
            carte=paquet.pop_carte()
            self.cartes.append(carte)
    def __str__(self):
        return f"Main de {self.etiquette}"

    def getCarte(self, index):
        return self.cartes[index]

    def setCarte(self, index, carte):
        self.cartes[index] = carte

    def ajouterCarte(self, carte):
        self.cartes.append(carte)

    def retirerCarte(self, index):
        return self.cartes.pop(index)

    def nombreCartes(self):
        return len(self.cartes)

    def montrerCarte(self, index):
        print(self.cartes[index])


from Carte import Carte
from random import shuffle
class Paquet:
    """Classe représentant un paquet"""
    def __init__(self, rempli: bool):
        """Initialisation d'un paquet"""
        self.cartes = []
        if rempli:
            self.remplir()
            self.battre()

    def __str__(self):
        """Affichage du paquet"""
        return '\n'.join(str(carte) for carte in self.cartes)


    def remplir(self):
        """Méthode qui initialise un paquet de cartes mélangé"""
        for couleur in range(4):
            for valeur in range(1,14):
                if(valeur>10):
                    carte = Carte(valeur,couleur,10)
                elif(valeur==13 and (couleur==1 or couleur==0)): #Roi rouge
                    carte = Carte(valeur,couleur,0)
                else:
                    carte = Carte(valeur,couleur,valeur)
                self.ajouter_carte(carte)

    def pop_carte(self):
        return self.cartes.pop()
        
    def ajouter_carte(self, carte: Carte):
        self.cartes.append(carte)
    def getCarte(self, index: int):
        return self.cartes[index]
    def printDerniereCarte(self):
        if not self.est_vide():
            print(self.cartes[-1])



    def battre(self):
        shuffle(self.cartes)
    def est_vide(self):
        return self.cartes == []
    

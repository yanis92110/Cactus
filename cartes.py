import random
from string import *
class Carte:
    """#0: Coeur 1:Carreau 2:Pique 3:Trefle"""
    def __init__(self, valeur, couleur, points):
        self.valeur = valeur
        self.couleur = couleur
        self.points = points

    # Méthode __str__ définie en dehors de __init__
    def __str__(self):
        nom_couleurs = ['coeur', 'carreau', 'pique', 'trefle']
        nom_valeurs = [None, 'as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']
        return '%s de %s' % (nom_valeurs[self.valeur], nom_couleurs[self.couleur])

class Paquet:

    def __init__(self):
        self.cartes = []
        for couleur in range(4):
            for valeur in range(1, 14):
                if(valeur > 10):
                    carte = Carte(valeur, couleur, 10)
                elif(valeur == 13 and couleur == 1):  # Roi de Carreau
                    carte = Carte(valeur, couleur, 0)
                elif(valeur == 13 and couleur == 0):  # Roi de Coeur
                    carte = Carte(valeur, couleur, 0)
                else:
                    carte = Carte(valeur, couleur, valeur)
                self.cartes.append(carte)

    def __str__(self):
        res = []
        for carte in self.cartes:
            res.append(str(carte))
        return '\n'.join(res)
    def pop_carte(self):
        return self.cartes.pop()
    def ajouter_carte(self, carte):
        self.cartes.append(carte)
    def battre(self):
        random.shuffle(self.cartes)

class Main(Paquet):
    def __init__(self, etiquette =''):
        super().__init__()
        self.cartes=[]
        self.etiquette=etiquette

def est_chiffre(caractere):
    if caractere.isdigit():
        return True
    else:
        return False
    



from Paquet import Paquet
from MainJoueur import MainJoueur
from time import *

class Partie():
    """Instance de jeu"""
    def __init__(self, nbjoueurs: int):
        """Constructeur qui prend en parametre un nombre de joueur.
        Il initialise un paquet rempli et mélangé ainsi qu'une défausse (Paquet vide).
        Puis il créer autant de mains que de nombre de joueurs"""
        self.paquet = Paquet(True)
        self.defausse = Paquet(False)
        self.tour = 0 #Nombre de tours
        self.continuer = True # Pour la boucle du jeu
        self.joueurs = [MainJoueur(self.paquet) for _ in range(nbjoueurs)]
    
    def pioche(self,joueur: MainJoueur):
        print("Entrée dans la pioche...")

        if self.paquet.est_vide:
            """Alors on remélange la défausse et elle devient le paquet courant"""
            derniere_carte = self.defausse.pop_carte
            self.paquet.cartes = self.defausse.cartes.copy()
            self.paquet.battre()
            self.defausse.cartes=[derniere_carte]

        carte_courante = self.paquet.pop_carte()
        print(f"Vous avez pioché la carte: {carte_courante}")
        print("Voulez vous la garder ou la défausser ? (g ou d)")
        reponse = input()
        while not(reponse=='g' or reponse=='d'):
            print("g ou d")
            reponse = input()
        if reponse=='d':
            self.defausse.ajouter_carte(carte_courante)
        else:
            print("Avec quelle carte voulez vous échanger ?")
            for i in range(MainJoueur.nombreCartes):
                print(f"Echanger avec la carte N°{i}")

    def jouer(self):
        #print(self.paquet)
        self.pioche(self.joueurs[0])
    
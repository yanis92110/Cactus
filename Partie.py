
from Carte import Carte
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
    
    def defausseToPaquet(self):
        """Méthode qui mélange la défausse et devient le paquet courant"""
        derniere_carte = self.defausse.pop_carte
        self.paquet.cartes = self.defausse.cartes.copy()
        self.paquet.battre()
        self.defausse.cartes=[derniere_carte]
    
    def pioche(self,joueur: MainJoueur):
        print("Entrée dans la pioche...")

        if self.paquet.est_vide():
            """Alors on remélange la défausse et elle devient le paquet courant"""
            self.defausseToPaquet()

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
            temp=0
            for i in range(joueur.nombreCartes()):
                temp+=1
                print(f"Echanger avec la carte N°{i}: {i}")
            
            reponse = input()
            while not reponse.isdigit() or int(reponse) >= temp:
                print(f"Entrer un nombre entre 0 et {temp-1}")
                reponse = input()
            reponse = int(reponse)
            temp = joueur.getCarte(reponse)
            joueur.setCarte(reponse,carte_courante)
            self.defausse.ajouter_carte(temp)

    def piocheDefausse(self,joueur: MainJoueur):
        print("Vous avez choisi de piocher dans la défausse !")
        if self.defausse.est_vide():
            print("Defausse vide tete de neuille.")
            self.pioche(joueur)
        else:
            carte_courante = self.defausse.pop_carte()
            print(f"La carte qui a été pioché est: {carte_courante}")
            print(f"Avec quelle carte voulez vous l'échanger ? (Entre 0 et {joueur.nombreCartes()})")
            reponse = input()
            self.defausse.ajouter_carte(joueur.getCarte(reponse))
            joueur.setCarte(reponse,carte_courante)
            print("Le joueur a défaussé la carte:")
            print(self.defausse.cartes[-1])

    def piocheOuDefausse(self,joueur):
        print(self.paquet.cartes[-1])
        reponse='a'
        while not(reponse=='p' or reponse=='d'):
            print("Que voulez vous faire ?\n d: piocher dans la défausse\n p: piocher dans la pioche")
            reponse = input()
        if reponse=='p':
            self.pioche(joueur)
        else:
            self.piocheDefausse(self,joueur)
    
    def carteSpeciale(self,carte_courante: Carte, joueur: MainJoueur):
        """10 Valet ou Dame sont des cartes spéciales"""
        if carte_courante.valeur==1:
            print("Vous venez de défausser un valet ! Vous pouvez échanger deux cartes de n'importe quel joueur ! (oui non)")
            reponse=input()
            if reponse=="oui":
                print("Avec quel joueur voulez vous échanger votre carte ?")
                print(f"Entrer 2 réponses entre 0 et {len(self.joueurs)-1}, vous etes joueur {self.joueurs.index(joueur)} (0 et 1 pour les joueurs 0 et 1)")
                #Verifs
                reponse1=input()
                reponse2=input()
                print(f"Quelle carte voulez vous échanger du joueur {reponse1}?")
                print(f"Entrer une valeur entre 0 et {len(self.joueurs[int(reponse1)].cartes)}")
                reponse=input()
                reponse=int(reponse)
                reponse1=int(reponse1)
                reponse2=int(reponse2)
                self.joueurs[reponse1].cartes[]
                



    def jouer(self):
        print(self.joueurs[0].getCarte(0))
        print(self.joueurs[0].getCarte(1))
        self.piocheOuDefausse(self.joueurs[0])
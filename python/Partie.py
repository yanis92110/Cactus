
from Carte import Carte
from Paquet import Paquet
from Joueur import Joueur
from time import *

class Partie():
    """Instance de jeu"""
    def __init__(self, nbjoueurs: int):
        """Constructeur qui prend en parametre un nombre de joueur.
        Il initialise un paquet rempli et mélangé ainsi qu'une défausse (Paquet vide).
        Puis il créer autant de mains que de nombre de joueurs"""
        self.paquet: Paquet = Paquet(True)
        self.defausse: Paquet = Paquet(False)
        self.tour: int = 0 #Nombre de tours
        self.continuer: bool = True # Pour la boucle du jeu
        self.joueurs: list = [Joueur(self.paquet,_) for _ in range(nbjoueurs)]
    
    def defausseToPaquet(self):
        """Méthode qui mélange la défausse et devient le paquet courant"""
        print("Mélange de la défausse...")
        derniere_carte = self.defausse.pop_carte
        self.paquet.cartes = self.defausse.cartes.copy()
        self.paquet.battre()
        self.defausse.cartes=[derniere_carte]
    
    def pioche(self,joueur: Joueur):
        print("Entrée dans la pioche...")
        sleep(1)

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

        sleep(1)

    def piocheDefausse(self,joueur: Joueur):
        print("Vous avez choisi de piocher dans la défausse !")
        sleep(1)
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
        sleep(2)

    def piocheOuDefausse(self,joueur: Joueur):
        if self.defausse.est_vide():
            print("Pas de carte dans la défausse !")
        else:
            print(self.defausse.cartes[-1])
        reponse='a'
        while not(reponse=='p' or reponse=='d'):
            print("Que voulez vous faire ?\n d: piocher dans la défausse\n p: piocher dans la pioche")
            reponse = input()
        if reponse=='p':
            self.pioche(joueur)
        else:
            self.piocheDefausse(joueur)
    
    def carteSpeciale(self,carte_courante: Carte, joueur: Joueur):
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
                print(f"Quelle carte voulez vous échanger du joueur {reponse1}?")
                print(f"Entrer une valeur entre 0 et {len(self.joueurs[int(reponse2)].cartes)}")
                carte1=input()
                carte2=input()
                reponse=int(reponse)
                carte1=int(carte1)
                carte2=int(carte2)
                self.joueurs[reponse1].cartes[carte1],self.joueurs[reponse2].cartes[carte2] = self.joueurs[reponse2].cartes[carte2],self.joueurs[reponse1].cartes[carte1]
        elif carte_courante.valeur==12:
            print("Vous avez défaussé une dame, vous pouvez regarder une de vos cartes !")
            print(f"Quelle carte voulez vous regarder ? Entre 0 et {joueur.nombreCartes()-1}")
            reponse=input()
            reponse=int(reponse)
            print(f"Votre {reponse}e carte est {joueur.getCarte(reponse)}")
        elif carte_courante.valeur == 10:
            print("Vous avez défaussé un 10, vous pouvez rejouer !")
            self.piocheOuDefausse(joueur)

                

    def cactus(self,joueur: Joueur):
        """Fonction qui demande si cactus et MAJ continuer"""
        print("Cactus ? (oui non)")
        reponse=input()
        if reponse =="oui" and self.continuer:
            print("CACTUSSZS")
            print("Dernier tour lancé !")
            sleep(1)
            self.continuer=False
        
    def premierTour(self):

        """Montre les cartes de chaque joueur au debut du tour"""
        for joueur in self.joueurs:
            joueur.montrerCarte(0)
            joueur.montrerCarte(1)
    def jouer(self):
                    self.tour += 1
                    print(f"Tour N°{self.tour}")
                    cpt = 0
                    joueur_cactus = None
                    for joueur in self.joueurs:
                        print("#####################")
                        print(f"Tour du joueur {joueur.etiquette} ({joueur})")
                        self.piocheOuDefausse(joueur)
                        print(f"Carte dans la défausse:")
                        self.defausse.printDerniereCarte()
                        self.carteSpeciale(self.defausse.getCarte(-1), joueur)
                        self.cactus(joueur)
                        if not self.continuer and joueur_cactus is None:
                            joueur_cactus = joueur
                        cpt += 1
                        # Le joueur qui a lancé le cactus rejoue
                        if joueur_cactus:
                            print("#####################")
                            print(f"Tour du joueur {joueur_cactus.etiquette} ({joueur_cactus})")
                            self.piocheOuDefausse(joueur_cactus)
                            print(f"Carte dans la défausse:")
                            self.defausse.printDerniereCarte()
                            self.carteSpeciale(self.defausse.getCarte(-1), joueur_cactus)

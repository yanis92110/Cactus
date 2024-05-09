import random
from string import *
import time
class Carte:
    """#0: Coeur 1:Carreau 2:Pique 3:Trefle"""
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

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
                carte = Carte(valeur, couleur)
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
        self.cartes=[]
        self.etiquette=etiquette

def est_chiffre(caractere):
    if caractere.isdigit():
        return True
    else:
        return False
    

paquet = Paquet()
paquet.battre()
defausse=[] #La défausse doit etre définie avant son appel dans les fonctions précédentes


def creerMain():
    main=Main()
    for i in range(0,4):
        carte=paquet.pop_carte()
        main.ajouter_carte(carte)
    return main
def montrerCarte(main):
    print("*********")
    print(main.cartes[0])
    print("*********")
    print("*********")
    print(main.cartes[1])
    print("*********")

def pioche():
        print("Vous allez piocher dans la pioche")
        time.sleep(1)
        temp=paquet.pop_carte()
        print(f"La carte qui a été pioché est: {temp}")
        print("Voulez vous garder la carte ou la défausser ? (g ou d)")
        reponse=input()
        while not(reponse=='g' or reponse=='d'):
            print("Entrez 'g' pour la garder ou 'd' pour la défausser:\n")
            reponse=input()
        if(reponse=='d'):
            defausse.append(temp)
        else:
            print("Avec quelle carte voulez vous échanger ? (1,2,3,4)")
            reponse=input()
            while reponse not in ["1","2","3","4"]:
                print("Avec quelle carte voulez vous échanger ? (1,2,3,4)")
                reponse=input()
            
            defausse.append(main.cartes[int(reponse)-1])
            #ATTENTION, vérifier si la main courante est bien celle du joueur
            main.cartes[int(reponse)-1]=temp
        print("Le joueur a défaussé une carte, carte de la défausse:")
        print(defausse[len(defausse)-1])
        time.sleep(2)


def prendreCarteDefausse():
        print("Vous allez piocher dans la défausse")
        temp=defausse.pop()
        print(f"La carte qui a été pioché est: {temp}")
        print("Avec quelle carte voulez vous échanger ? (1,2,3,4)")
        reponse=input()
        while reponse not in ["1","2","3","4"]:
            print("Avec quelle carte voulez vous échanger ? (1,2,3,4)")
            reponse=input()
        defausse.append(main.cartes[int(reponse)-1])
        main.cartes[int(reponse)-1]=temp
    
def piocheOuDefausse():
        print("Que voulez vous faire ?\n d: piocher dans la défausse\n p: piocher dans la pioche")
        reponse=input()
        while not(reponse=='p' or reponse=='d'):
            print("Que voulez vous faire ?\n d: piocher dans la défausse\n p: piocher dans la pioche")
            reponse=input()
        if(reponse=='p'):
            pioche()
        else:
            prendreCarteDefausse()

def carteSpeciale():
    #temp=defausse[len(defausse)-1]
    temp=paquet.pop_carte()
    while(temp.valeur!="valet" or temp.valeur!="dame" or temp.valeur!="10"):
        temp=paquet.pop_carte()
        print(f"Carte de la défausse :{temp.valeur}")
        time.sleep(1)
    if(temp.valeur=="valet"):
        print("Vous venez de défausser un valet ! Vous pouvez échanger des cartes dans le jeu !\n Voulez vous échanger des cartes ? (oui/non)")
        reponse=input()
        if(reponse=="oui"):
            print("Avec quels joueurs voulez vous échanger de cartes ? (Entrez: 1 puis 2 pour joueur 1 et 2)")
            print(f"Entrer une réponse entre 1 et {nbjoueurs}")
            reponse1=input()
            reponse2=input()
            """while not(1<=reponse<=nbjoueurs):
                print("Avec quels joueurs voulez vous échanger de cartes ? (Entrez: 1 2 pour joueur 1 et 2)")
                print(f"Entrer une réponse entre 1 et {nbjoueurs}")"""
            while not(1<=int(reponse1)<=nbjoueurs):
                print("Avec quels joueurs voulez vous échanger de cartes ? (Entrez: 1 puis 2 pour joueur 1 et 2)")      #ATTENTION il va yavoir pb car on teste dans le if avec des str
                print(f"Entrer une réponse entre 1 et {nbjoueurs}")
                reponse1=input()
                reponse2=input()
            while not(1<=int(reponse2)<=nbjoueurs):
                print("Avec quels joueurs voulez vous échanger de cartes ? (Entrez: 1 puis 2 pour joueur 1 et 2)")
                print(f"Entrer une réponse entre 1 et {nbjoueurs}")
                reponse1=input()
                reponse2=input()
            print(f"Quelles carte du joueur {reponse1} voulez vous échanger ?")
            #Chiantos, je finis apres
    if(temp.valeur=="dame"):
        print("Vous avez défaussé une dame, vous pouvez regarder une de vos cartes !")
        time.sleep(3)
        print("Quelle carte voulez vous regarder ? (1,2,3,4)")
        reponse=input()
        while reponse not in ["1","2","3","4"]:
            print("Quelle carte voulez vous regarder ? (1,2,3,4)")
            reponse=input()
        print(f"Votre {reponse}e carte est: {main.cartes[int(reponse)]}")
        return
    if(temp.valeur=="10"):
        print("Vous avez défaussé un 10, vous pouvez rejouer !")
        time.sleep(3)
        piocheOuDefausse()
        return

def cactus():
    # si c'est en javascript proposer un bouton qui active la fonction
    return


#Debut du jeu

print("Entrer le nombre de joueurs:")
nbjoueurs=input()

while not(nbjoueurs.isdigit() and 2<= int(nbjoueurs)<=10):
    print("Entrer le nombre de joueurs (entre 2 et 10):")
    nbjoueurs=input()

nbjoueurs=int(nbjoueurs)
tour=0
mains_joueurs=[]

for i in range(nbjoueurs):
    main=creerMain()
    mains_joueurs.append(main)
for i, main in enumerate(mains_joueurs):
    print(f"Cartes du joueur {i+1}:")
    montrerCarte(main)
finjeu=True
while(finjeu):
    tour+=1
    print(f"Tour {tour} du joueur {i}")
    time.sleep(4)
    if defausse:
        print(f"Carte dans la défausse: {defausse[-1]}")
        time.sleep(4)
        piocheOuDefausse()
    else:
        print("La défausse est vide.")
        pioche()


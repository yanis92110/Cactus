from cartes import *
#import interface
import time


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

    print(main.cartes[1])
def paquet_vide(paquet):
    if(paquet.cartes == []):
        derniere_carte=defausse.pop()
        paquet.cartes=defausse.cartes.copy()
        paquet=paquet.battre
        defausse=[derniere_carte]

def pioche(joueur,paquet):
        main=mains_joueurs[joueur]
        print("Vous allez piocher dans la pioche")
        time.sleep(1)
        paquet_vide(paquet)
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
        print(defausse[-1])
        time.sleep(2)


def prendreCarteDefausse(joueur):
        main=mains_joueurs[joueur]
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
        print("Le joueur a défaussé une carte, carte de la défausse:")
        print(defausse[-1])
        time.sleep(2)
    
def piocheOuDefausse(joueur):
        main=mains_joueurs[joueur]
        print("Que voulez vous faire ?\n d: piocher dans la défausse\n p: piocher dans la pioche")
        reponse=input()
        while not(reponse=='p' or reponse=='d'):
            print("Que voulez vous faire ?\n d: piocher dans la défausse\n p: piocher dans la pioche")
            reponse=input()
        if(reponse=='p'):
            pioche(joueur,paquet)
        else:
            prendreCarteDefausse(joueur)

def carteSpeciale(temp,joueur):
    main=mains_joueurs[joueur]
    if(temp.valeur==11):
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
            carte1="0"
            while carte1 not in ["1","2","3","4"]:
                print(f"Quelles carte du joueur {reponse1} voulez vous échanger ? (1,2,3,4)")
                carte1=input()
            carte2="0"
            while carte2 not in ["1","2","3","4"]:
                print(f"Quelles carte du joueur {reponse2} voulez vous échanger ? (1,2,3,4)")
                carte2=input()
            reponse1=int(reponse1)
            reponse2=int(reponse2)
            carte1=int(carte1)
            carte2=int(carte2)
            main_joueur1 = mains_joueurs[reponse1-1]
            main_joueur2 = mains_joueurs[reponse2-1]
            temp2=main_joueur1[carte1]
            main_joueur1[carte1] = main_joueur2[carte2]
            main_joueur2[carte2] = temp2
            print(f"La {carte1}e carte du joueur {reponse1} a été échangée avec la {carte2}e du joueur {reponse2} ! \n")
            return
            
    if(temp.valeur==12):
        print("Vous avez défaussé une dame, vous pouvez regarder une de vos cartes !")
        time.sleep(3)
        print("Quelle carte voulez vous regarder ? (1,2,3,4)")
        reponse=input()
        while reponse not in ["1","2","3","4"]:
            print("Quelle carte voulez vous regarder ? (1,2,3,4)")
            reponse=input()
        print(f"Votre {reponse}e carte est: {main.cartes[int(reponse)-1]}")
        return
    if(temp.valeur==10):
        print("Vous avez défaussé un 10, vous pouvez rejouer !")
        time.sleep(3)
        piocheOuDefausse(joueur)
        carteSpeciale(defausse[-1],count-1)
        return

def cactus():
    # si c'est en javascript proposer un bouton qui active la fonction
    global finjeu
    reponse=""
    while reponse not in ["oui", "non"]:
        print("Cactus ? (oui ou non)\n")
        reponse=input()
        #lowercase
    if(reponse=="non"):
        return
    else:
        print("CACTUS !\n")
        finjeu=False
        return


#Debut du jeu

# Exemple d'utilisation
if __name__ == "__main__":
    jeu = Jeu()
    jeu.start_game(4)
    print([str(carte) for carte in jeu.get_hand(0)])  # Affiche la main du joueur 1
"""
carte=Carte(11,0,10)
print(carte.valeur)

print("Entrer le nombre de joueurs:")
nbjoueurs=input()

while not(nbjoueurs.isdigit() and 2<= int(nbjoueurs)<=10):
    print("Entrer le nombre de joueurs (entre 2 et 10):")
    nbjoueurs=input()

nbjoueurs=int(nbjoueurs)
tour=0
mains_joueurs=[Main(f'Joueur {i+1}') for i in range(nbjoueurs)]

for _ in range(4):
    for main in mains_joueurs:
        if paquet.cartes:
            main.ajouter_carte(paquet.pop_carte())
print("\nMains des joueurs après distribution :")
for main in mains_joueurs:
    montrerCarte(main)
finjeu=True


count=0
while(finjeu):
    temp=False
    if(count==0):
        tour+=1
    count+=1
    print(f"Tour {tour} du joueur {count}")
    time.sleep(3)
    if defausse:
        print(f"Carte dans la défausse: {defausse[-1]}")
        time.sleep(3)
        piocheOuDefausse(count-1)
        carteSpeciale(defausse[-1],count-1)
        
    else:
        print("La défausse est vide.")
        pioche(count-1,paquet)
        carteSpeciale(defausse[-1],count-1)
    if(count==nbjoueurs):
        count=0
    cactus()
    if temp:
        finjeu=False
    if not finjeu:
        print("Dernier tour !")
        temp=True
        finjeu=True
    
#Quelqu'un a fait cactus
print("Fin du jeu ! Calcul des points...")
time.sleep(1)
points_joueurs=[]
for joueur in range(nbjoueurs):
    for cartes in mains_joueurs[joueur].cartes:
        points_joueurs.append(0)
        points_joueurs[joueur] += cartes.points
print("Total des points:\n")
for joueur in range(nbjoueurs):
    print(f"Joueur {joueur+1}: {points_joueurs[joueur]} points !")
"""
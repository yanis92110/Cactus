import time
from fonctions import *
#Debut du jeu

### Tests
print("Entrer le nombre de joueurs:")
nbjoueurs=input()

while not(nbjoueurs.isdigit() and 2<= int(nbjoueurs)<=10):
    print("Entrer le nombre de joueurs (entre 2 et 10):")
    nbjoueurs=input()

nbjoueurs=int(nbjoueurs)
tour=0
#global mains_joueurs
mains_joueurs=[Main(f'Joueur {i+1}') for i in range(nbjoueurs)]

for _ in range(4):
    for main in mains_joueurs:
        if paquet.cartes:
            main.ajouter_carte(paquet.pop_carte())
print("\nMains des joueurs après distribution :")
for main in mains_joueurs:
    montrerCarte(main)
finjeu=False

### Debut du jeu
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

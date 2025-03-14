from cartes import *



paquet = Paquet()
paquet.battre()
defausse=[] #La défausse doit etre définie avant son appel dans les fonctions précédentes



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

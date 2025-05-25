from Partie import Partie

print("Combien de joueurs ?")

jeu = Partie(2)
jeu.premierTour()
while jeu.continuer:
    jeu.jouer()


#### Calcul des scoresp

for joueur in jeu.joueurs:
    for carte in joueur.cartes:
        joueur.addScore(carte.valeur)
    print(f"Score de Joueur {joueur.etiquette}: {joueur.score}")
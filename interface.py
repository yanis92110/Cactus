import pygame
import sys
from cartes import *
from jeu import *


# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
window_size = (1080, 720)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jeu de Cartes")

images_path_joueur=[]
print(len(mains_joueurs))
print(mains_joueurs[0])


for main in mains_joueurs:
    for i in range(0,4):
        images_path_joueur.append((f"static/img/{main.cartes[i]}"))
print(images_path_joueur)


loaded_images = []

for path in images_path_joueur:
    image = pygame.image.load(f"{path}.png")
    image = pygame.transform.scale(image,(50,100))
    loaded_images.append(image)
image_positions=[]
x=-100
y=0
for position in loaded_images:
    if(x>200):
        x=-100
        y+=300
    x+=200
    image_positions.append((x,y))



# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.mouse.get_focused:
            print("Appuyé !")

    # Remplir l'arrière-plan
    window.fill((0, 128, 0))  # Vert foncé pour ressembler à une table de jeu

    # Afficher chaque image à sa position respective || Affiche les carte devoilees a la position voulue
    #for i, image in enumerate(loaded_images):
     #   window.blit(image, image_positions[i])

    #Affiche les cartes cachées a la position voulue
    for i, image in enumerate(loaded_images):
        window.blit(pygame.image.load("static/img/base.jpg"),image_positions[i])
    window.blit(pygame.image.load("static/img/base.jpg"),(900,0))
    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
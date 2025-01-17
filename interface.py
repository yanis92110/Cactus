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
    image = pygame.transform.scale(image,(150,200))
    loaded_images.append(image)
image_positions=[]
x=-100
y=0
for position in loaded_images:
    if(x>800):
        y+=300
    x+=200
    image_positions.append((x,y))

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplir l'arrière-plan
    window.fill((0, 128, 0))  # Vert foncé pour ressembler à une table de jeu

    # Afficher chaque image à sa position respective
    for i, image in enumerate(loaded_images):
        window.blit(image, image_positions[i])

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
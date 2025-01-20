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



for main in mains_joueurs:
    for i in range(0,4):
        images_path_joueur.append((f"static/img/{main.cartes[i]}"))



loaded_images = []

for path in images_path_joueur:
    image = pygame.image.load(f"{path}.png")
    image = pygame.transform.scale(image,(100,150))
    loaded_images.append(image)
image_positions=[]
x=250
y=0
i=0
print(i%2)
for position in loaded_images:
    if i%1:
        y+=200
        x=250
    if i>=4:
        y=150
        x=-100
    x+=100
    i+=1
    image_positions.append((x,y))
"""for position in loaded_images:

    if(x>200):
        x=-100
        y+=300
    x+=100
    image_positions.append((x,y))
"""
# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.mouse.get_pressed:
            print("Appuyé !")

    # Remplir l'arrière-plan
    window.fill((0, 128, 0))  # Vert foncé pour ressembler à une table de jeu

    # Afficher chaque image à sa position respective || Affiche les carte devoilees a la position voulue
    #for i, image in enumerate(loaded_images):
     #   window.blit(image, image_positions[i])

    #Affiche les cartes cachées a la position voulue
    scaled_image=pygame.image.load("static/img/base.jpg")
    scaled_image=pygame.transform.scale(scaled_image,(100,150))
    for i, image in enumerate(loaded_images):
        

        window.blit(scaled_image,image_positions[i])
    window.blit(pygame.image.load("static/img/base.jpg"),(900,0))
    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
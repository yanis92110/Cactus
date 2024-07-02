import pygame
import sys
#from cartes import *
#from jeu import *
# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
window_size = (1200, 1000)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jeu de Cartes")

images_path_joueur=[]
for main in mains_joueurs:
    for i in range(0,3):
        images_path_joueur.append((0,main[i]))
print(images_path_joueur)
images_path = ["img/cinq de coeur.png","img/as de trefle.png"]

loaded_images = []

for path in images_path:
    image = pygame.image.load(path)
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
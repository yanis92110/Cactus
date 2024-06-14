import pygame
import sys
#import cartes
#import jeu
# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jeu de Cartes")

images_path = []

loaded_images = []

for path in images_path:
    image = pygame.image.load(path)
    image = pygame.transform.scale(image,(150,200))
    loaded_images.append(image)


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
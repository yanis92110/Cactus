import pygame
import sys
from Partie import Partie


class Fenetre():
    def __init__(self):
        # Initialiser Pygame
        pygame.init()
        # Définir les dimensions de la fenêtre
        window_size = (1080, 720)
        window = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Cactus")
        self.partie

    def start(self):
        print("Combien de joueurs ?")
        nb = int(input())
        self.partie = Partie(nb)
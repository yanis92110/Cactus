import requests
from bs4 import BeautifulSoup
import os

class Carte:
    """Représente une carte à jouer standard."""

    def __init__(self, couleur=0, valeur=2):
        self.couleur = couleur
        self.valeur = valeur

    # à l'intérieur de la classe Carte :
    noms_couleurs = ['trèfle', 'carreau', 'cœur', 'pique']
    noms_valeurs = [None, 'as', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'valet', 'dame', 'roi']

    @classmethod
    def liste_noms_cartes(cls):
        noms_cartes = []
        for couleur in cls.noms_couleurs:
            for valeur in cls.noms_valeurs[1:]:
                noms_cartes.append('%s de %s' % (valeur, couleur))
        return noms_cartes

    def __str__(self):
        return '%s de %s' % (Carte.noms_valeurs[self.valeur],
                             Carte.noms_couleurs[self.couleur])

def extract_card_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Créer une liste de tous les noms de cartes
    noms_cartes = Carte.liste_noms_cartes()

    # Parcourir chaque nom de carte
    for nom_carte in noms_cartes:
        # Rechercher les balises <img> avec l'attribut "alt" correspondant au nom de carte
        images = soup.find_all('img', alt=lambda x: x and nom_carte in x.lower())
        # Télécharger chaque image correspondante
        for img in images:
            img_url = img['src']
            download_image(img_url)

def download_image(url):
    # Obtenir le nom de fichier à partir de l'URL
    filename = url.split('/')[-1]
    # Télécharger l'image et enregistrer localement
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Image téléchargée : {filename}")

# URL de la page contenant les images de cartes à jouer
wiki_url = 'https://fr.wikipedia.org/wiki/Carte_%C3%A0_jouer'
# Appeler la fonction pour extraire et télécharger les images de cartes
extract_card_images(wiki_url)

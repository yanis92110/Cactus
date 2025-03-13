class Carte:
    """#0: Coeur 1:Carreau 2:Pique 3:Trefle"""
    def __init__(self, valeur, couleur, points):
        self.valeur = valeur
        self.couleur = couleur
        self.points = points

    # Méthode __str__ définie en dehors de __init__
    def __str__(self):
        nom_couleurs = ['coeur', 'carreau', 'pique', 'trefle']
        nom_valeurs = [None, 'as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']
        return '%s de %s' % (nom_valeurs[self.valeur], nom_couleurs[self.couleur])

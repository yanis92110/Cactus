import os

# Dictionnaire pour mapper les nombres en lettres vers leurs équivalents numériques
lettres_vers_nombres = {
    "un": "1",
    "deux": "2",
    "trois": "3",
    "quatre": "4",
    "cinq": "5",
    "six": "6",
    "sept": "7",
    "huit": "8",
    "neuf": "9",
    "dix": "10",
}

# Chemin du dossier contenant les fichiers
chemin_dossier = "static/img"

# Parcourir tous les fichiers du dossier
for fichier in os.listdir(chemin_dossier):
    # Vérifier si c'est un fichier et pas un dossier
    chemin_complet = os.path.join(chemin_dossier, fichier)
    if os.path.isfile(chemin_complet):
        # Extraire le nom du fichier et son extension
        nom, extension = os.path.splitext(fichier)

        # Remplacer les nombres en lettres par leurs équivalents numériques
        for mot, nombre in lettres_vers_nombres.items():
            if mot in nom:
                nom = nom.replace(mot, nombre)

        # Générer le nouveau chemin
        nouveau_nom = f"{nom}{extension}"
        chemin_nouveau = os.path.join(chemin_dossier, nouveau_nom)

        # Renommer le fichier
        os.rename(chemin_complet, chemin_nouveau)
        print(f"Renommé : {fichier} -> {nouveau_nom}")

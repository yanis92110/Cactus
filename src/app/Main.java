package app;

import modele.Paquet;
import vue.FenetreJeu;
import controleur.Controleur;

import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
        	Partie partie = new Partie(2);
            //Paquet paquet = new Paquet();
            FenetreJeu fenetre = new FenetreJeu();
            fenetre.setVisible(true);
            new Controleur(partie,partie.getJoueurCourant(), fenetre);

            

        });
    }
}

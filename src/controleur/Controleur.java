package controleur;

import modele.Paquet;
import modele.Carte;
import modele.Joueur;
import vue.FenetreJeu;

import java.awt.event.*;

import app.EffetCarte;
import app.Partie;

public class Controleur {
    private Partie partie;
    private FenetreJeu fenetre;
    private Joueur joueurCourant;
    private Carte carteCourante;

    public Controleur(Partie partie, Joueur j, FenetreJeu fenetre) {
        this.partie = partie;
        this.fenetre = fenetre;
        this.joueurCourant = j;

        commencerTour();

        fenetre.getBoutonPioche().addActionListener(e -> piocherDepuisPaquet());
        fenetre.getBoutonPiocheDefausse().addActionListener(e -> piocherDepuisDefausse());

        fenetre.getBoutonDefausser().addActionListener(e -> defausserCarte());
        fenetre.getBoutonGarder().addActionListener(e -> garderCarte());
    }

    private void commencerTour() {
        System.out.println("Tour " + partie.getTour() + " de " + joueurCourant.getNom());
        fenetre.afficherCarte(null);

        fenetre.getBoutonPioche().setVisible(true);
        fenetre.getBoutonPiocheDefausse().setVisible(true);
        fenetre.getBoutonGarder().setVisible(false);
        fenetre.getBoutonDefausser().setVisible(false);
    }

    private void piocherDepuisPaquet() {
        carteCourante = partie.getPaquet().piocher();
        afficherCarteEtBoutons();
    }

    private void piocherDepuisDefausse() {
        carteCourante = partie.getDefausse().piocher();
        afficherCarteEtBoutons();
    }

    private void afficherCarteEtBoutons() {
        if (carteCourante != null) {
            fenetre.afficherCarte(carteCourante);
        } else {
            fenetre.afficherCarte(null);
        }
        fenetre.getBoutonGarder().setVisible(true);
        fenetre.getBoutonDefausser().setVisible(true);
        fenetre.getBoutonPioche().setVisible(false);
        fenetre.getBoutonPiocheDefausse().setVisible(false);
    }

    private void defausserCarte() {
        partie.defausserCarte(carteCourante);
        fenetre.afficherDefausse(partie.getDefausse().getDerniereCarte());
        EffetCarte effet = partie.carteSpeciale();

        if (effet == EffetCarte.REJOUER) {
            System.out.println(joueurCourant.getNom() + " rejoue !");
            commencerTour(); // ne change pas de joueur
        } else {
            changerJoueur();
        }
    }

    private void garderCarte() {
        joueurCourant.ajouterCarte(carteCourante); // méthode à créer dans Joueur
        changerJoueur();
    }

    private void changerJoueur() {
        partie.joueurSuivant();
        joueurCourant = partie.getJoueurCourant();
        commencerTour();
    }
}

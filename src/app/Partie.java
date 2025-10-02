package app;

import java.util.ArrayList;

import modele.*;
public class Partie {
	private Paquet paquet;
	private Paquet defausse;
	private int tour;
	private boolean continuer;
	private ArrayList<Joueur> joueurs;
	private int joueurCourant = 0;
	
	public Partie(int nbJoueurs) {
		this.paquet = new Paquet();
		this.defausse = new Paquet(false);
		this.tour = 1;
		this.continuer = true;
		this.joueurs = new ArrayList<Joueur>(); // <-- initialise la liste
		for(int i=0;i<nbJoueurs;i++) {
			this.joueurs.add(new Joueur("Joueur "+i, this.paquet));
		}
	}
	public int getTour() {
		return this.tour;
	}
	public Joueur getJoueursIndice(int i) {
		return this.joueurs.get(i);
	}
	public ArrayList<Joueur> getJoueurs(){
		return this.joueurs;
	}
	public boolean continuer() {
		return this.continuer;
	}
	
	public void defausseToPaquet() {
		System.out.println("Mélange de la défausse...");
		ArrayList<Carte> derniereCarte = null;
		derniereCarte.add(this.defausse.getDerniereCarte());
		Paquet.copyCartes(this.defausse.getCartes(), this.paquet.getCartes()); //la défausse devient le jeu
		this.paquet.battre();
		
		this.defausse.setCartes(derniereCarte);
	}
	
	public void defausserCarte(Carte c) {
		this.defausse.ajouterCarte(c);
	}
	
	public EffetCarte carteSpeciale() {
		if (this.defausse.estVide()) return EffetCarte.AUCUN;
		
		String valeur = this.defausse.getDerniereCarte().getNom().split(" ")[0];
		switch(valeur) {
			case "10":
				return EffetCarte.REJOUER;
			case "Valet":
				return EffetCarte.ECHANGER;
			case "Dame":
				return EffetCarte.VOIR;
			default:
				return EffetCarte.AUCUN;
				
		}
	}

	public Paquet getPaquet() {
		return paquet;
	}
	public void setPaquet(Paquet paquet) {
		this.paquet = paquet;
	}
	public Paquet getDefausse() {
		return defausse;
	}
	public void setDefausse(Paquet defausse) {
		this.defausse = defausse;
	}
	public Joueur getJoueurCourant() {
		return this.joueurs.get(joueurCourant);
	}
	public void setJoueurCourant(int i) {
		this.joueurCourant = i;
	}
	public void joueurSuivant() {
	    this.joueurCourant = (this.joueurCourant + 1) % this.joueurs.size();
	}

}
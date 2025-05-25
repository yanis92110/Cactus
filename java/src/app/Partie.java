package app;
import java.util.ArrayList;
import jeu.*;
public class Partie {
	private Paquet paquet;
	private Paquet defausse;
	private int tour;
	private boolean continuer;
	private ArrayList<Joueur> joueurs;
	
	public Partie(int nbJoueurs) {
		this.paquet = new Paquet(true);
		this.defausse = new Paquet(false);
		this.tour = 1;
		this.continuer = true;
		for(int i=0;i<nbJoueurs;i++) {
			this.joueurs.add(new Joueur("Joueur "+i, this.paquet));
		}
	}
	public void defausseToPaquet() {
		System.out.println("Mélange de la défausse...");
		ArrayList<Carte> derniereCarte = null;
		derniereCarte.add(this.defausse.getDerniereCarte());
		Paquet.copyCartes(this.defausse.getCartes(), this.paquet.getCartes()); //la défausse devient le jeu
		this.paquet.battre();
		
		this.defausse.setCartes(derniereCarte);
	}
	public void pioche(Joueur j) {
		System.out.println("Entrée dans la pioche...");
		//sleep
		
		if(this.paquet.estVide()) {
			//Alors on remélange la defausse et devient le paquet courant
			this.defausseToPaquet();
		}
		Carte carteCourante = this.paquet.getDerniereCarte();
		System.out.println("Vous avez piocché la carte: "+carteCourante +"\nVoulez vous la garder ou la défausser ?");
		//au lieu de faire avec scanner faire avec l'interface directement ca y est frere
		
		
	}
}

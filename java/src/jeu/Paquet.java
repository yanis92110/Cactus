package jeu;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Objects;

public class Paquet {
	private ArrayList<Carte> cartes;
	
	public Paquet(boolean rempli) {
		this.cartes = new ArrayList<>();
		if(rempli) {
			this.remplir();
			this.battre();
		}
	}
	public void remplir() {
		this.cartes.clear();
		for(int couleur=0;couleur<4;couleur++) {
			for(int valeur=1;valeur<14;valeur++) {
				int points;
				if(valeur>10) {
					points = 10;
				}
				else if(valeur==13 && (couleur==1 || couleur==0)) {
					points = 0;
				}
				else {
					points = valeur;
				}
				Carte carte = new Carte(valeur,couleur,points);
				this.cartes.add(carte);
			}
		}
	}
	public void battre() {
		Collections.shuffle(this.cartes);
	}
	public void ajouterCarte(Carte carte) {
		this.cartes.add(carte);
	}
	public Carte getCarte(int i) {
		return this.cartes.get(i);
	}
	public Carte getDerniereCarte() {
		return this.cartes.getLast();
	}
	public boolean estVide() {
		return this.cartes.isEmpty();
	}
	public ArrayList<Carte> getCartes() {
		return cartes;
	}
	public void setCartes(ArrayList<Carte> cartes) {
		this.cartes = cartes;
	}
	public static void copyCartes(ArrayList<Carte> src, ArrayList<Carte> dest) {
		dest.clear();
		for(Carte c : src) {
			dest.add(c);
		}
	}
	@Override
	public int hashCode() {
		return Objects.hash(cartes);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Paquet other = (Paquet) obj;
		return Objects.equals(cartes, other.cartes);
	}
}

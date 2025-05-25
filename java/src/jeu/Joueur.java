package jeu;
import java.util.ArrayList;
import java.util.Objects;
public class Joueur {
	private String nom;
	private ArrayList<Carte> cartes;
	private int score=0;
	
	public Joueur(String nom,Paquet paquet) {
		this.nom = nom;
		for(int i=0;i<4;i++) {
			this.cartes.add(paquet.getDerniereCarte());
		}
	}
	public Carte getCarte(int i) {
		return this.cartes.get(i);
	}
	public void setCarte(Carte c, int i) {
		this.cartes.set(i, c);
	}
	public void ajouterCarte(Carte c) {
		this.cartes.addLast(c);
	}
	public Carte retirerCarte(int i) {
		return this.cartes.remove(i);
	}
	public int nombreCartes() {
		return this.cartes.size();
	}
	public void ajouterScore(int i) {
		this.score+=i;
	}
	public String getNom() {
		return nom;
	}
	public void setNom(String nom) {
		this.nom = nom;
	}
	public ArrayList<Carte> getCartes() {
		return cartes;
	}
	public void setCartes(ArrayList<Carte> cartes) {
		this.cartes = cartes;
	}
	public int getScore() {
		return score;
	}
	public void setScore(int score) {
		this.score = score;
	}
	@Override
	public String toString() {
		String temp = "";
		for(Carte c : this.cartes) {
			temp = temp + c + "\n";
		}
		return temp;
	}
	@Override
	public int hashCode() {
		return Objects.hash(cartes, nom, score);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Joueur other = (Joueur) obj;
		return Objects.equals(cartes, other.cartes) && Objects.equals(nom, other.nom) && score == other.score;
	}
}

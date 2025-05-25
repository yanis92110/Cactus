package jeu;

import java.util.Objects;

public class Carte {
	private int valeur;
	private int couleur;
	private int points;
	
	public Carte(int valeur, int couleur,int points) {
		this.valeur = valeur;
		this.couleur = couleur;
		this.points = points;
	}

	public int getValeur() {
		return valeur;
	}

	public void setValeur(int valeur) {
		this.valeur = valeur;
	}

	public int getCouleur() {
		return couleur;
	}

	public void setCouleur(int couleur) {
		this.couleur = couleur;
	}

	public int getPoints() {
		return points;
	}

	public void setPoints(int points) {
		this.points = points;
	}

	@Override
	public int hashCode() {
		return Objects.hash(couleur, points, valeur);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Carte other = (Carte) obj;
		return Objects.equals(couleur, other.couleur) && points == other.points && valeur == other.valeur;
	}

	@Override
	public String toString() {
		return "Carte [valeur=" + valeur + ", couleur=" + couleur + ", points=" + points + "]";
	}
}

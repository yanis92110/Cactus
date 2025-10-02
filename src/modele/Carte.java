package modele;

import java.util.Objects;

public class Carte {
	private int valeur;
	private int couleur;
	
	private String nom;
	private String cheminImage;
	
	public Carte(String nom, String chemin,int valeur, int couleur) {
		this.nom = nom;
		this.cheminImage = chemin;
		this.valeur = valeur;
		this.couleur = couleur;
		
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




	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Carte other = (Carte) obj;
		return Objects.equals(couleur, other.couleur) && valeur == other.valeur;
	}

	@Override
	public String toString() {
		return "Carte [valeur=" + valeur + ", couleur=" + couleur + "]";
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getCheminImage() {
		return cheminImage;
	}

	public void setCheminImage(String cheminImage) {
		this.cheminImage = cheminImage;
	}
}
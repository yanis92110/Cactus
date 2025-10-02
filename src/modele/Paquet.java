package modele;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Objects;

public class Paquet {
	private ArrayList<Carte> cartes;
	
    public Paquet() {
        this.cartes = new ArrayList<Carte>();

        String[] nomsValeurs = {"as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"};
        String[] nomsCouleurs = {"coeur", "carreau", "trefle", "pique"};

        for (int couleur = 0; couleur < nomsCouleurs.length; couleur++) {
            for (int valeur = 1; valeur <= 13; valeur++) {
                String nom = nomsValeurs[valeur - 1] + " de " + nomsCouleurs[couleur];
                String cheminImage = nom + ".png";
                Carte carte = new Carte(nom, cheminImage, valeur, couleur);
                cartes.add(carte);
            }
        }

        Collections.shuffle(cartes); // mélange au départ
        
    }
    
    public Paquet(boolean bool) {
    	//Créer un paquet vide
    	this.cartes = new ArrayList<Carte>();
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
    public Carte piocher() {
        if (!cartes.isEmpty()) {
            return cartes.remove(0);
        }
        return null;
    }
}
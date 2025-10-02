package vue;

import javax.swing.*;
import modele.Carte;
import java.awt.*;

public class FenetreJeu extends JFrame {
    private JButton boutonPioche;
    private JLabel labelCarteCentre;
    private JLabel labelPioche;
    private JLabel labelDefausse;
    private JButton boutonGarder;
    private JButton boutonDefausser;
    private JButton boutonPiocheDefausse;

    public FenetreJeu() {
        setTitle("Jeu de cartes - MVC");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // --- PANEL HAUT (pioche + défausse) ---
        JPanel panelHaut = new JPanel(new BorderLayout());
        JPanel panelCartes = new JPanel(new FlowLayout(FlowLayout.RIGHT, 20, 10)); // alignement à droite

        labelPioche = new JLabel(new ImageIcon("C:\\Program Files\\Python312\\code\\perso\\Cactus\\Cactus\\static\\img\\base.png"));
        labelDefausse = new JLabel(new ImageIcon("C:\\Program Files\\Python312\\code\\perso\\Cactus\\Cactus\\static\\img\\base.png"));


        panelCartes.add(labelPioche);
        panelCartes.add(labelDefausse);
        panelHaut.add(panelCartes, BorderLayout.EAST);

        add(panelHaut, BorderLayout.NORTH);

        // --- CENTRE : carte piochée ---
        labelCarteCentre = new JLabel("Clique sur 'Piocher' pour commencer", SwingConstants.CENTER);
        labelCarteCentre.setFont(new Font("Arial", Font.BOLD, 18));
        add(labelCarteCentre, BorderLayout.CENTER);

        // --- BAS : boutons ---
        boutonPioche = new JButton("Piocher");
        boutonGarder = new JButton("Garder");
        boutonDefausser = new JButton("Défausser");

        boutonGarder.setVisible(false);
        boutonDefausser.setVisible(false);

        JPanel panelBoutons = new JPanel(new FlowLayout());
        panelBoutons.add(boutonPioche);
        panelBoutons.add(boutonGarder);
        panelBoutons.add(boutonDefausser);

        add(panelBoutons, BorderLayout.SOUTH);
        boutonPiocheDefausse = new JButton("Piocher dans la défausse");
        boutonPiocheDefausse.setVisible(false); // caché au début
        panelBoutons.add(boutonPiocheDefausse);

    }

    public JButton getBoutonPioche() { return boutonPioche; }
    public JButton getBoutonGarder() { return boutonGarder; }
    public JButton getBoutonDefausser() { return boutonDefausser; }

    public void afficherCarte(Carte c) {
        if (c == null) {
            labelCarteCentre.setIcon(null);
            labelCarteCentre.setText("Plus de cartes !");
            return;
        }
        ImageIcon icone = new ImageIcon("C:\\Program Files\\Python312\\code\\perso\\Cactus\\Cactus\\static\\img\\" + c.getCheminImage());
        labelCarteCentre.setIcon(icone);
        labelCarteCentre.setText(c.getNom());
        labelCarteCentre.setHorizontalTextPosition(SwingConstants.CENTER);
        labelCarteCentre.setVerticalTextPosition(SwingConstants.BOTTOM);
    }
    public void afficherDefausse(Carte c) {
        if (c == null) {
            labelDefausse.setIcon(new ImageIcon("C:\\Program Files\\Python312\\code\\perso\\Cactus\\Cactus\\static\\img\\base.png"));
            labelDefausse.setText("Défausse vide");
        } else {
            ImageIcon icone = new ImageIcon("C:\\Program Files\\Python312\\code\\perso\\Cactus\\Cactus\\static\\img\\" + c.getCheminImage());
            
            labelDefausse.setIcon(icone);
            labelDefausse.setText(c.getNom());
            labelDefausse.setHorizontalTextPosition(SwingConstants.CENTER);
            labelDefausse.setVerticalTextPosition(SwingConstants.BOTTOM);
        }
    }


    public JButton getBoutonPiocheDefausse() {
        return boutonPiocheDefausse;
    }

}

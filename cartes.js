class Cartes{
    constructor(self,valeur,couleur){
        self.valeur=valeur;
        self.couleur=couleur;
    }
    strr(self){
        noms_couleurs=["coeur","carreau","pique","trefle"];
        noms_valeurs=["as","2","3","4","5","6","7","8","9","10","valet","dame","roi"];
        return " de "+noms_valeurs[self.valeur] +noms_couleurs[self.couleur];
    }

}
class Paquet{
    constructor(){
        self.cartes=[]
        for(couleur in Range(4)){
            for(valeur in Range(1,14)){
                carte=Cartes(valeur,couleur);
                self.cartes.append(carte);
            }
        }
    }
    strrr(self){
        res=[];
        for(carte in self.cartes){
            res.append(str(carte));
        }
        return "\n".join(res);
    }
    pop_carte(self){
        return self.cartes.pop();
    }
    ajouter_carte(self,carte){
        self.cartes.append(carte);
    }
}

export interface IVoiture{

    marque : string;
    modele : string;
    annee : string;
}

export class Voiture implements IVoiture{ 

    marque : string;
    modele : string;
    annee : string;

    constructor(marque : string, modele: string, annee : string){
        this.marque = marque;
        this.modele = modele;
        this.annee = annee;
    }
}
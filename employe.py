class Employe:

    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None


    def afficher_information(self):
        print("Employer:", self.nom , self.prenom)
        print("Permis:", self.numeroPermis)
        if self.voitureService:
            print("Voiture:", self.voitureService.marque, self.voitureService.matricule)
        else:
            print("Aucune voiture assignée")

    def affecter_voiture(self, voiture):
        if self.voitureService is not None:
            print("cet employer a deja une voiture ")
        elif voiture.chauffeur is not None:
            print("cette voiture est deja assignée ")
        else :
            self.voitureService = voiture
            voiture.chauffeur = self
            print("voiture est deja assignée")

    def retirer_voiture(self):
        if self.voitureService is None:
            print("pas de voiture a retirer")
        else:
            self.voitureService.chauffeur = None
            self.voitureService = None
            print("voiture est retirer")
class Employe:

    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None


    def afficher_information(self):
        print("Employer:", self.nom , self.prrenom)
        print("Permis:", self.numeroPermis)
        if self.voitureService:
            print("Voiture:", self.voitureService.marque, self.voitureService.nom, self.voitureService.matricule)
        else:
            print("Aucune voiture assignée")

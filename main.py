from employe import Employe
from voiture import Voiture

emp1=Employe("1","Barry","Saliou")
emp2=Employe("2","Diallo","Ali")

v1=Voiture("A1",2026,"NISAN",5500)
v2=Voiture("A2",2026,"TOYOTA",7000)


emp1.afficher_information()
emp1.affecter_voiture(v1)
print()
emp1.retirer_voiture()
print()
emp1.afficher_information()

emp2.afficher_information()
print()
emp2.affecter_voiture(v2)
print()
emp2.retirer_voiture()
print()
emp2.afficher_information()
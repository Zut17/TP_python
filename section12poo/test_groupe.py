from etudiant import Etudiant
from groupe import Groupe

g = Groupe()
g.ajouter(Etudiant("Amina", 12.0, 15.5))
g.ajouter(Etudiant("Brice", 10.0, 11.0))
g.ajouter(Etudiant("Chloé", 14.0, 16.0))

meilleur = g.etudiants[0]
for e in g.etudiants:
    if e.moyenne() > meilleur.moyenne():
        meilleur = e

print(f"Moyenne générale : {g.moyenne_generale():.2f}")
print(f"Meilleur étudiant : {meilleur.nom} ({meilleur.moyenne():.2f})")
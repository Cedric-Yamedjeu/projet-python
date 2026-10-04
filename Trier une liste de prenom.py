# Trier une liste de prenom

from pathlib import Path

chemin_dossier = Path(r"C:\Users\bruno\Downloads\prenoms.txt")

# Lire le dossier
liste_prenom = chemin_dossier.read_text()
# Remplacer les "." par les ","
liste_prenom = liste_prenom.replace("." , ",")
#print(liste_prenom)
# Créer une liste
liste_prenom = liste_prenom.split()
#print(liste_prenom)
# Supprimer les "," sur les prénoms
liste_prenom_clean = [prenom.strip(",") for prenom in liste_prenom]
#print(liste_prenom_clean)
liste_prenom_trier = sorted(liste_prenom_clean)
#print(liste_prenom_trier)

# Créer un fichier text 
chemin = Path.home() / "Downloads" / "prenoms_ordonné.txt"
#chemin.touch()
# Transformer la liste en texte 
texte_final = "\n".join(liste_prenom_trier)
# Mettre la liste ordonnée dans le nouveau fichier

chemin.write_text(texte_final, encoding="utf-8")


# Proff 

#with open("/Users/thibh/Documents/prenoms.txt", "r") as f:
 #   lines = f.read().splitlines()

#prenoms = []
#for line in lines:
 #   prenoms.extend(line.split())

#prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

#with open("/Users/thibh/Documents/prenoms_final.txt", "w") as f:
 #   f.write("\n".join(sorted(prenoms_final)))

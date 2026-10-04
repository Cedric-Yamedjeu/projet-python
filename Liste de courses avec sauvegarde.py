# Liste de courses avec sauvegarde sur le disque dur
from pathlib import Path
import json
import os



# CUR_DIR = os.path.dirname(__file__) / prof
# LISTE_PATH = os.path.join(CUR_DIR, "liste.json") / prof
# if os.path.exists(LISTE_PATH):
  #  with open(LISTE_PATH, "r") as f:
   #     LISTE = json.load(f)
#else:
 #   LISTE = []


dossier_script = Path(__file__).parent / "test_course.json"
#print(dossier_script)
chemin = os.path.join(dossier_script)
#print(chemin)
liste_course = ["tomate", "piment", "viande", "condiments"]

menu = [
"1. Ajouter un élément à la liste de courses",
"2. Retirer un élément de la liste de courses",
"3. Afficher les éléments de la liste de courses",
"4. Vider la liste de courses",
"5. Quitter le programme",
]

if os.path.exists(chemin):
    print("Le fichier existe")
    with open(dossier_script, "r", encoding="utf-8") as f:
        liste_course = json.load(f)

   
    while True:
        print("Choisir parmis ses 5 actions: ")
        for i, element in enumerate(menu):
            print(f"{element}")
        action = input("Veuillez choisir votre action: ")
        if action not in ["1","2", "3", "4", "5"]:
            action = input("Action non valide. Veuillez faire un choix valide: ")
            
        else:
            if action == "1":
                ajouter = input("Veuillez ajouter un élément à la liste: ")
                liste_course.append(ajouter)
                print(f"Votre élément a été ajouter à la liste de courses: {liste_course}")
                with open(chemin, "w") as f:
                    json.dump(liste_course, f, indent=4)
                

            elif action == "2":
                retirer = input("Veuillez retirer un élément à la liste: ")
                if retirer not in liste_course:
                    retirer = input("Absent de la liste. Veuillez retirer un élément à la liste de courses: ")
                    continue
                else:
                    liste_course.remove(retirer)
                    print(f"Votre élément a été retirer de la liste de courses: {liste_course}")
                    with open(chemin, "w") as f:
                        json.dump(liste_course, f, indent=4)

            elif action == "3":
                print(f"Les éléments de la liste de courses sont: {liste_course}")
                with open(chemin, "w") as f:
                    json.dump(liste_course, f, indent=4)

            elif action == "4":
                liste_course.clear()
                print(f"Votre liste de courses a été vider: {liste_course}")
                with open(chemin, "w") as f:
                    json.dump(liste_course, f, indent=4)

            elif action == "5":
                with open(chemin, "w") as f:
                    json.dump(liste_course, f, indent=4)
                break
else:
    print("Le fichier n'existe pas")
    liste_course = []

print("-"*70)
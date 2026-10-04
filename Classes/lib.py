



from pathlib import Path
import json


class Liste(list):
    def __init__(self, nom):
        self.nom = nom


    def ajouter(self, element):
        if not isinstance(element, str):
            print(f"Erreur, le terme {element} n'est pas une chaine de caractère.")
            return False
        elif isinstance(element, str):
            if not element in self:
                self.append(element)
                return True
            else:
                print(f"{element} est déjà dans la liste.")
                return False


    def enlever(self, element):
        if not element in self:
            print(f"{element} n'est pas dans la liste.")
            return False
        else:
            self.remove(element)
            return True


    def afficher(self):
        if self == []:
                    print(f"Ma liste de {self.nom} est vide.")
                    return False
        else:
            print(f"Ma liste de {self.nom} est : ")
            for element in self:
                print(f"- {element}")
                

       


    def sauvegarder(self):
        CUR_DIR = Path.home() / "FORMATION_PYTHON" / "Classes" / f"{self.nom}.json"
        if not Path.exists(CUR_DIR):
            CUR_DIR.touch()

        with open(CUR_DIR, "w") as f:
            json.dump(self, f, ensure_ascii=False, indent=4)

        return True



l = Liste("Courses")

l.ajouter("Tomates")
l.ajouter("huile")
l.ajouter("oignons")
l.enlever("huile")
print(l)
l.afficher()

l.sauvegarder()
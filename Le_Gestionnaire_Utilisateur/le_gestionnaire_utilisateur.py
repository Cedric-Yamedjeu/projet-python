# Le Gestionnaire d'Utilisateur

from tinydb import TinyDB, where
from faker import Faker
import re  # nettoyer et remplacer
import string  # récupérer tous les symboles de ponctuations
from pathlib import Path

fake = Faker(locale="fr_FR")


class Users:
    # Base de données
    db = TinyDB(Path(__file__).resolve().parent / "Data.json", indent=4, ensure_ascii=False)

    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    # Représentation
    def __repr__(self) -> str:
        return f" {self.full_name} {self.phone_number} {self.address}"

    def __str__(self):
        return f"Informations de l'utilisateur : \n{self.full_name} \n{self.phone_number} \n{self.address}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Récupération de l'adresse et le téléphone d'un membre de la base de données
    @property
    def db_instance(self):
        return Users.db.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))

    # Vérifier si un utilisateur existe
    def exists(self):
        return bool(self.db_instance)

    # Supprimer un utilisateur de la base de données
    def delete(self):
        if self.exists:
            #assert self.db_instance is not None
            Users.db.remove(doc_ids=[self.db_instance.doc_id])

    # Méthode pour vérifier les noms et les numéros de téléphones
    def _checks(self):
        self._check_names()
        self._check_phone_numbers()

    def _check_phone_numbers(self):
        # Suppression des caractères
        phone_digits = re.sub(r"[+()\s]*", "", self.phone_number)
        # print(phone_digits)
        if len(phone_digits) < 10 or not phone_digits.isdigit():
            raise ValueError(f"Numéro {self.phone_number} ivalide.")

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("Le prénom et le nom sont obligatoire.")

        special_caracteres = string.punctuation + string.digits
        for charactere in self.first_name + self.last_name:
            if charactere in special_caracteres:
                raise ValueError(f"Le nom {self.full_name} n'est pas valide.")

    # Méthode pour sauvegarder les données après vérification
    def save(self, validate_data=False):
        if validate_data:
            self._checks()

        if self.exists():
            return None

        else:
            return Users.db.insert(self.__dict__)


# Récupération de toutes les données
def get_all_users() -> list[Users]:
    return [Users(**user) for user in Users.db.all()]


if __name__ == "__main__":
    #Richard = Users("Richard", "Millet")
    #Richard.delete()
    get_all_users()











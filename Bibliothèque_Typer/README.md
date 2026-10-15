# Recherche et suppression de fichiers par extension (CLI)

Petit outil en ligne de commande, écrit en Python avec la bibliothèque [Typer](https://typer.tiangolo.com/), qui permet de **rechercher** ou de **supprimer** tous les fichiers d'un dossier selon leur extension (`.txt`, `.py`, `.csv`, etc.).

Projet réalisé pendant ma formation Python pour découvrir la création d'applications en ligne de commande.

## Fonctionnalités

- Recherche de tous les fichiers d'une extension donnée, y compris dans les sous-dossiers
- Choix du dossier à explorer (par défaut : le dossier courant)
- Suppression des fichiers trouvés, avec une demande de confirmation avant toute suppression
- Messages colorés dans le terminal et barre de progression
- Aide intégrée avec `--help`

## Technologies

- Python 3.9 ou supérieur
- [Typer](https://typer.tiangolo.com/) (création de la ligne de commande)
- `pathlib` (parcours des dossiers et des fichiers)

## Installation

```bash
git clone https://github.com/Cedric-Yamedjeu/Formation_Python.git
cd Formation_Python/Bibliotheque_Typer

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

pip install typer
```

## Utilisation

Le programme propose trois commandes.

### 1. `run` : choisir le dossier et l'action

```bash
# Chercher les fichiers .py dans un dossier précis
python application_recherche_extensions.py run py C:\Users\mon_nom\Documents

# Chercher dans le dossier courant (sans préciser de dossier)
python application_recherche_extensions.py run txt

# Supprimer les fichiers .tmp d'un dossier (confirmation demandée)
python application_recherche_extensions.py run tmp C:\Users\mon_nom\Documents --delete
```

| Élément | Rôle |
|---|---|
| `extension` | Extension à chercher, **sans le point** (`py`, pas `.py`) |
| `directory` | Dossier à explorer (facultatif, dossier courant par défaut) |
| `--delete` | Supprime les fichiers trouvés après confirmation |

### 2. `search` : raccourci de recherche

```bash
python application_recherche_extensions.py search py
```

Cherche les fichiers `.py` dans le dossier courant.

### 3. `delete` : raccourci de suppression

```bash
python application_recherche_extensions.py delete tmp
```

Supprime les fichiers `.tmp` du dossier courant, après confirmation.

### Aide

```bash
python application_recherche_extensions.py --help
```

## Attention

La suppression est **définitive** : les fichiers ne passent pas par la corbeille. Lance d'abord une recherche pour voir ce qui sera concerné, et teste d'abord sur un dossier de test.

## Structure du projet

```
Bibliotheque_Typer/
├── application_recherche_extensions.py   # Application principale (commandes run, search, delete)
└── README.md
```

## Ce que ce projet m'a appris

- Créer des commandes avec arguments et options grâce à Typer
- Parcourir une arborescence de fichiers avec `pathlib`
- Sécuriser une action risquée avec une confirmation
- Gérer les erreurs simples (dossier inexistant) et afficher des messages clairs

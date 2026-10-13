# Analyse de données avec Python et pandas

Trois notebooks Jupyter réalisés pendant ma formation Python pour apprendre à **nettoyer, filtrer, agréger et visualiser des données** avec pandas.

## Contenu

| Notebook | Données | Ce qu'il fait |
|---|---|---|
| `datascience.ipynb` | `data.csv` (1 000 ventes) | Prise en main de pandas : exploration, sélection, filtres, nettoyage, nouvelles colonnes |
| `analyse_ventes.ipynb` | `data.csv` | Analyse des ventes : indicateurs, regroupements et graphiques |
| `analyse_netflix.ipynb` | `netflix_titles.csv` (7 787 titres) | Questions d'analyse sur le catalogue Netflix |

## 1. `datascience.ipynb` : manipuler un tableau de données

- Explorer un jeu de données : `head`, `tail`, `shape`, liste des colonnes
- Sélectionner des lignes et des colonnes (`loc`, index sur une colonne)
- Filtrer : par genre, par pays (`isin`), par montant (`price_paid >= 6`)
- Supprimer des lignes et des colonnes (`drop`, `del`)
- Repérer et traiter les valeurs manquantes (`isnull`, `dropna`, `fillna`)
- Convertir une colonne texte (`"$5.36"`) en nombre décimal
- Créer une colonne calculée : le prix restant après taxe (`price_total = price_paid × (1 − tax / 100)`)

## 2. `analyse_ventes.ipynb` : analyser et visualiser des ventes

- Statistiques descriptives (`describe`) et prix moyen
- Nombre de ventes par pays
- Montants dépensés par genre (`groupby`)
- Évolution du montant total payé par jour (courbe)
- Répartition par genre (camembert) et par pays (diagramme en barres) avec matplotlib

## 3. `analyse_netflix.ipynb` : questions sur le catalogue Netflix

Quelques réponses obtenues sur 7 787 titres :

- **Pays les plus représentés** : États-Unis (2 555 titres), Inde (923), Royaume-Uni (397)
- **Titres par année de sortie** : pic en 2018 (1 121 titres) sur la période 2012-2021
- **Durée moyenne des films** : environ 99 minutes
- Liste des réalisateurs présents sur la plateforme

## Technologies

- Python 3
- pandas
- matplotlib
- Jupyter Notebook

## Installation

```bash
git clone https://github.com/TON-PSEUDO/Formation_Python.git
cd Formation_Python/datascience

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

pip install pandas matplotlib notebook
jupyter notebook
```

Ouvre ensuite le notebook de ton choix et lance les cellules dans l'ordre. Les fichiers `.csv` doivent rester dans le même dossier que les notebooks.

## Structure du dossier

```
datascience/
├── datascience.ipynb
├── analyse_ventes.ipynb
├── analyse_netflix.ipynb
├── data.csv
├── netflix_titles.csv
└── README.md
```

## Ce que ces notebooks m'ont appris

- Lire un fichier CSV et inspecter rapidement un jeu de données
- Nettoyer des données : valeurs manquantes, conversion de types
- Filtrer, trier et regrouper pour répondre à une question précise
- Produire des graphiques lisibles pour présenter des résultats

## Pistes d'amélioration

- Convertir la colonne `date` en vrai format date pour trier correctement l'évolution dans le temps
- Compter séparément chaque pays quand un titre Netflix en compte plusieurs
- Ajouter des indicateurs (variation, moyenne par période) et un export Excel

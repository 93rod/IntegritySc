# IntegritySc - Malicious Package Finder

IntegritySc est un outil de détection de paquets malveillants dans les fichiers téléchargés. Il utilise des techniques d'analyse de chaînes de caractères et de comparaison avec une liste de signatures connues pour identifier les indicateurs de paquets malveillants.

## Fonctionnalités

- Analyse des fichiers téléchargés à la recherche d'indicateurs de paquets malveillants.
- Comparaison des fichiers avec une liste de signatures connues de paquets malveillants.
- Extraction des métadonnées des paquets .deb, .rpm et .zip.
- Génération d'un rapport des résultats de l'analyse.

## Installation

git clone https://github.com/93rod/IntegritySc.git
cd integritysc
pip install -r requirements.txt

## Utilisation

Placez les fichiers à analyser dans le dossier spécifié. Vous pouvez donner le chemin que vous voulez à la variable "dossier_projet"
Exécutez le script principal :
python package_finder.py
> Consultez le rapport généré pour obtenir les résultats de l'analyse.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :
Fork du dépôt.

Créez une nouvelle branche pour vos fonctionnalités ou corrections :
git checkout -b nouvelle-fonctionnalite

Faites les modifications nécessaires et committez vos changements :
git commit -m "Ajout d'une nouvelle fonctionnalité"

Poussez les modifications vers votre dépôt distant :
git push origin nouvelle-fonctionnalite

Créez une Pull Request pour demander l'incorporation de vos modifications.

## Auteurs
Votre Nom (@93rod) - lien vers votre profil GitHub https://github.com/93rod

import os
import hashlib

def cal_hash(fichier):
    """Calcule le hash MD5 d'un fichier"""
    hasher = hashlib.md5()
    with open(fichier, 'rb') as f:
        for bloc in iter(lambda: f.read(4096), b''):
            hasher.update(bloc)
    return hasher.hexdigest()

def analyz_file(fichier, mal_hash):
    """Analyse un fichier à la recherche d'indicateurs de paquet malveillant"""
    hash_file = cal_hash(fichier)

    if hash_file in mal_hash:
        print(f"Indicateur de paquet malveillant trouvé dans le fichier : {fichier}")
        return True
    return False

def load_signatures(file_path):
    """Charge les signatures connues depuis un fichier"""
    with open(file_path, 'r') as f:
        signatures = set(line.strip() for line in f)
    return signatures

def analyser_dependances(scan_repo, mal_hash):
    """Analyse les dépendances d'un projet"""
    resultats = []
    for racine, sous_dossiers, fichiers in os.walk(scan_repo):
        for fichier in fichiers:
            path_file = os.path.join(racine, fichier)
            if analyz_file(path_file, mal_hash):
                resultats.append(path_file)
    return resultats

def rapport(resultats):
    """Génère un rapport basé sur les résultats de l'analyse"""
    if resultats:
        print("Rapport d'analyse :")
        for resultat in resultats:
            print(resultat)
    else:
        print("Aucun indicateur de paquet malveillant trouvé.")

def main():
    scan_repo = "~/Téléchargements/" #ajouter le dossier que vous voulez scanner  "
    mal_hash = load_signatures("~/IntegritySc/MD5 Hahses.txt")
    resultats = analyser_dependances(scan_repo, mal_hash)

    rapport(resultats)

if __name__ == "__main__":
    main()

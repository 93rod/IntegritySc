import os
import hashlib

def cal_hash(fichier):
    """Calcule le hash MD5 d'un fichier"""
    hasher = hashlib.md5()
    with open(fichier, 'rb') as f:
        for bloc in iter(lambda: f.read(4096), b''):
            hasher.update(bloc)
    return hasher.hexdigest()

def analyz_file(fichier, signatures_connues):
    """Analyse un fichier à la recherche d'indicateurs de paquet malveillant"""
    hash_file = cal_hash(fichier)

    if hash_file in signatures_connues:
        print(f"Indicateur de paquet malveillant trouvé dans le fichier : {fichier}")
        return True
    return False

def load_signatures(file_path):
    """Charge les signatures connues depuis un fichier"""
    with open(file_path, 'r') as f:
        signatures = set(line.strip() for line in f)
    return signatures

def analyser_dependances(dossier_projet, signatures_connues):
    """Analyse les dépendances d'un projet"""
    resultats = []
    for dossier_racine, sous_dossiers, fichiers in os.walk(dossier_projet):
        for fichier in fichiers:
            path_file = os.path.join(dossier_racine, fichier)
            if analyz_file(path_file, signatures_connues):
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
    dossier_projet = "/home/uzi/Téléchargements/"
    signatures_connues = load_signatures("/home/uzi/Programmation/python/Uzi-M_PackageFinde/MD5 Hahses.txt")
    resultats = analyser_dependances(dossier_projet, signatures_connues)

    rapport(resultats)

if __name__ == "__main__":
    main()

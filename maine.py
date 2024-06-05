import json


if __name__ == '__main__':
    with open("utilisateur.json", "r") as fichier:
        f1 = json.load(fichier)

    lol = "asd"
    for iu in f1:
        print("le nom est:", iu["nom"])
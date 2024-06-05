from mdp_decryp import verif_mdp
import json


def login(nom, mdp):
    with open("utilisateur.json", 'r') as fichier:
        f1 = json.load(fichier)
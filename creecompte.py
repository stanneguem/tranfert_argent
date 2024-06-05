from random import randint, shuffle, sample
import json
from mdp_protect import hash_mdp


def newcompte():
    nom = input("Entre un nom d'utilisateur")
    mdp = input("Entre un mot de passe")
    mdpc = input("Confirmer le mdp")
    if mdp == mdpc:
        mdp_h = hash_mdp(mdp)
        reset1 = input("Entre un moot de passe de recuperatiuon")
        reset = hash_mdp(reset1)
        solde = 0
        numero1 = [randint(1, 1000) for i in range(20)]
        shuffle(numero1)
        nu = sample(numero1, 12)
        numero = "".join(str(nu) for nu in nu)
        data = {
            "nom": nom,
            "code compte": mdp_h,
            "numero compte": numero,
            "solde": solde,
            "reset token": reset
        }
        with open("utilisateur.json", 'a') as fichier:
            json.dump(data, fichier, indent=4)
            fichier.close()
    else:
        print('veuillez recommence l\'action les mots de passe ne correspondent pas')
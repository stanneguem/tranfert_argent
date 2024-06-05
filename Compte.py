from datetime import datetime


class Compte:
    def __init__(self, nomclient, codecompte, numerocompte, solde, coderecup):
        self.nomclient = nomclient
        self.codecompte = codecompte
        self.numerocompte = numerocompte
        self.solde = solde
        self.coderecup = coderecup

    def depot(self, montant):
        self.solde += montant
        print(f"la somme de {montant} a ete ajoute a votre compte le {datetime.now()} votre  nouveau solde est de"
              f" {self.solde}")

    def retrait(self, montant):
        self.solde -= montant
        print(f"la somme de {montant} a ete retire de votre compte le {datetime.now()} votre  nouveau solde est de"
              f" {self.solde}")

    def transeft(self, montant, receveur):
        if montant <= 0:
            print(f"vous ne pouvez pas effectuer une transaction de {montant} FCFA")
        if self.solde < montant:
            print("vous ne dispose pas d'asser de moyen pour effectue cette transaction")

        receveur.solde += montant
        self.solde -= montant
        print(f"vous avez tranfere la somme de {montant} au compte {receveur.numerocompte} votre nouveau solde est"
              f"de {self.solde}")
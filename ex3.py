
from abc import ABC, abstractmethod


# Classe abstraite
class Paiement(ABC):

    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit etre positif")

        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


# Paiement par carte bancaire
class CarteBancaire(Paiement):

    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        self.numero = numero
        self.cvv = cvv

    def payer(self):
        if len(self.numero) != 16 or not self.numero.isdigit():
            return "Numero de carte invalide"

        if len(self.cvv) != 3 or not self.cvv.isdigit():
            return "CVV invalide"

        return "Paiement par carte bancaire de " + str(self._montant) + " euros effectue."


# Paiement par PayPal
class PayPal(Paiement):

    def __init__(self, montant, email, token):
        super().__init__(montant)
        self.email = email
        self.token = token

    def payer(self):
        return "Paiement PayPal de " + str(self._montant) + " euros pour " + self.email + " effectue."


# Paiement par Crypto
class Crypto(Paiement):

    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return "Paiement Crypto de " + str(self._montant) + " euros via " + self.reseau + " effectue."


# Fonction de traitement des paiements
def traiter_paiements(liste):

    for paiement in liste:
        print(paiement.payer())


# Programme principal
if __name__ == "__main__":

    p1 = CarteBancaire(200, "4532015112830366", "123")
    p2 = CarteBancaire(350, "4716108999716531", "456")

    p3 = PayPal(150, "ahmed@gmail.com", "TOKEN123")
    p4 = PayPal(250, "sara@gmail.com", "TOKEN456")

    p5 = Crypto(500, "WALLET001", "BTC")
    p6 = Crypto(700, "WALLET002", "ETH")

    paiements = [p1, p2, p3, p4, p5, p6]

    print("===== SYSTEME DE PAIEMENT =====")

    traiter_paiements(paiements)

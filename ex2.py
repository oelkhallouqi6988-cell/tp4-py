
from abc import ABC, abstractmethod
import math


# Classe abstraite
class Forme(ABC):

    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        resultat = self.aire()
        return self.__class__.__name__ + " - aire : " + format(resultat, ".2f")


# Classe Cercle
class Cercle(Forme):

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon * self.rayon


# Classe Rectangle
class Rectangle(Forme):

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


# Classe Triangle
class Triangle(Forme):

    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2


# Classe Carre
class Carre(Rectangle):

    def __init__(self, cote):
        super().__init__(cote, cote)


# Programme principal
if __name__ == "__main__":

    f1 = Cercle(3)
    f2 = Rectangle(4, 5)
    f3 = Triangle(6, 2)
    f4 = Carre(4)

    formes = [f1, f2, f3, f4]

    print("===== Calcul des aires =====")

    for forme in formes:
        print(forme)

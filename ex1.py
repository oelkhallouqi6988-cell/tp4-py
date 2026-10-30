
# Classe mere
class Animal:
    def parler(self):
        print("Animal en train de parler...")


# Classe Chien
class Chien(Animal):
    def parler(self):
        print("Ouaf !")


# Classe Chat
class Chat(Animal):
    def parler(self):
        print("Miaou !")


# Classe Vache
class Vache(Animal):
    def parler(self):
        print("Meuh !")


# Classe Robot (Duck Typing)
class Robot:
    def parler(self):
        print("Bonjour ! Je suis un robot.")


# Fonction pour faire parler les animaux
def faire_parler(animal):
    animal.parler()


# Programme principal
a1 = Chien()
a2 = Chat()
a3 = Chien()
a4 = Vache()
a5 = Robot()

liste = [a1, a2, a3, a4, a5]

print("===== Les animaux et le robot =====")

for element in liste:
    faire_parler(element)

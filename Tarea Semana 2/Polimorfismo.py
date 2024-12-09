
class Animal:

    def hacer_son(self):
        pass

class Perro(Animal):
    def hacer_soni(self):
        print("Guauu!")

class Gato(Animal):
    def hacer_soni(self):
        print("Miau!")

# Polimorfismo
def hacer_soni_de_animal(animal: Animal):
    animal.hacer_son()

perro = Perro()
gato = Gato()


hacer_soni_de_animal(gato)   # "Miau!"

hacer_soni_de_animal(perro)  # "Guauu!"
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_son(self):
        pass


class Gato(Animal):
    def hacer_son(self):
        print("Miau!")

class Perro(Animal):
    def hacer_son(self):
        print("Gua!")

# Uso de la abstracción

gato = Gato()
gato.hacer_son()  # "Miau!"

perro = Perro()
perro.hacer_son()  # "Gua!"
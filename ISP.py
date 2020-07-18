#!/usr/bin/python3

'''
Principio de Segregación de Interfaces
'''
# Interfaz AVE
class BirdInterface():

    # Método Comer
    def eat(self):
        return 'I can eat!'

# Interfaz Ave Voladora
class FlyingBirdInterface():

    # Método Volar
    def fly(self):
        return 'I can fly!'
# Interfaz Ave Nadadora
class SwimmingBridInterface():

    # Método Nadar
    def swim(self):
        return 'I can swim!'

# Clase Loro
class Parrot(BirdInterface, FlyingBirdInterface):

    # Método Comer
    def eat(self):
        return 'I can eat!'

    # Método Volar
    def fly(self):
        return 'I can fly!'

# Clase Pingüino
class Penguin(BirdInterface, SwimmingBridInterface):

    # Método Comer
    def eat(self):
        return 'I can eat!'

    # Método Nadar
    def swim(self):
        return 'I can swim!'


def main():

    # Intancia de Loro
    parrot = Parrot()
    print(f'Perrot: { parrot.eat() } and { parrot.fly() }')

    # Instancia de Pinguino
    penguin = Penguin()
    print(f'Penguin: { penguin.eat() } and { penguin.swim() }')

main()
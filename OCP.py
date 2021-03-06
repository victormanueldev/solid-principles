#!/usr/bin/python3

'''
Principio de Abierto/Cerrado
'''
class Car:
    
    # Metdo Abstracto
    def avg_car_price(self):
        pass


class Renault(Car):

    # Retorna el valor promedio de un Auto Renault
    def avg_car_price(self):
        return 10000


class Audi(Car):

    # Retorna el valor promedio de un Auto Audi
    def avg_car_price(self):
        return 25000

class Mercedes(Car):

    # Retorna el valor promedio de un Auto Mercedes
    def avg_car_price(self):
        return 27000

# Imprime en pantalla el precio promedio de cada tipo de auto
def print_avg_car_price(cars):
    for car in cars:
        print(car.avg_car_price())

def main():

    car_renault     = Renault()
    car_audi        = Audi()
    car_mercedes    = Mercedes()
    cars = [ car_renault, car_audi, car_mercedes ]

    print_avg_car_price(cars)

# Inicia la ejecución del programa
main()

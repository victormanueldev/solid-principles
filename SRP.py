#!/usr/bin/python3

'''
Principio de Responsabilidad Unica
'''

class Car:

    # Constructor de la clase
    def __init__(self, mark):
        self.mark = mark
    
    # Retorna la marca del coche
    def get_car_mark(self):
        return self.mark


class CarDB:

    # Guarda un coche en la base de datos
    def save_car_DB(self, car):
        # ...
        return car

    # Elimina un coche de la base de datos
    def delete_car_DB(self, car):
        # ...
        return 'Car deleted'

def main():

    # Obetner la marca del carro
    car = Car('Audi')
    print(f'Car Mark: {car.get_car_mark()} \n')

    # Save Car into Dabase
    car_to_save = CarDB()
    print(f'Car: { car_to_save.save_car_DB(car) } save successfully!')

    car_to_delete = CarDB()
    print(f'{ car_to_delete.delete_car_DB(car) }')

main()
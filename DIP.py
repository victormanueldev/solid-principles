#!/usr/bin/python3

'''
Principio de Inversión de Dependecias
'''

# Interfaz de Conexión
class ConnectionInterface():

    # Abstract - Obtener Datos
    def get_data(self):
        pass
    
    # Abstract - Establecer Datos
    def set_data(self):
        pass

class ServiceDatabase(ConnectionInterface):

    # Obtener Datos
    def get_data(self):
        return 'Data from Database'
    
    # Establcer Datos
    def set_data(self):
        return 'Data has been set'

class APIService(ConnectionInterface):
    
    # Obtener Datos
    def get_data(self):
        return 'Data from Database'

    # Establcer Datos
    def set_data(self):
        return 'Data has been set'


def main():

    # Instancia del Servicio de Base de datos
    db_service = ServiceDatabase()
    print(f'Database Service: { db_service.get_data() }, { db_service.set_data() }')

    # Instancia de la API
    api_service = APIService()
    print(f'API Service: {api_service.get_data() }, { api_service.set_data() } ')

main()
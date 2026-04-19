class Telefono:
    def __init__ (self, id, marca, modelo, almacenamiento, precio):
        self.__id = id
        self.__marca = marca 
        self.__modelo = modelo 
        self.__almacenamiento = almacenamiento 
        self.__precio = precio

    def get_id(self):
        return self.__id
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_modelo(self):
        return self.__almacenamiento
    def get_precio(self):
        return self.__precio

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
     
    def set_id(self, id):
        self.__id = id
    def set_marca(self, marca):
        self.__marca = marca 
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def set_almacenamiento(self, almacenamiento):
        self.__almacenamiento = almacenamiento
    def set_precio(self, precio):
        self.__precio = precio
    
    def info(self):
        print(f"{self.__id}, {self.__marca}, {self.__modelo}, {self.__almacenamiento}, {self.__precio}")
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
    def get_almacenamiento(self):
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
    
    def precio_con_iva(self):
        return self.__precio * 1.16 

    def clasificar_gama(self):
        if self.__precio < 5000:
            return "Gama baja"
        elif self.__precio < 15000:
            return "Gama media"
        else:
            return "Gama alta"

t1 = Telefono(1, "Iphone", "14 pro", 256, 14000)
print(t1.get_id())
print(t1.get_marca())
print(t1.get_modelo())          
print(t1.get_precio())

t1.set_precio(10000)
print(t1.get_precio())

t1.info()
print("precio con IVA: ", t1.precio_con_iva())
print("Es gama: ", t1.clasificar_gama())
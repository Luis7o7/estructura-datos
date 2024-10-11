class Vehiculo:
    def __init__(self, marca:str, conbustible:str, gasolina:int, gasolina_actual:int):
        self.marca=marca
        self.conbustible=conbustible 
        self.gasolina=gasolina
        self.gasolina_actual=gasolina_actual
        self.en_marcha= False
    def encender(self):
        if  self.gasolina_actual<0.10*self.gasolina:
            print("No hay suficiente gasolina para encender el vehiculo")
        else:    
            print("El vehiculo esta encendido")
            self.en_marcha=True

    def marcha(self):
        while self.gasolina_actual> 0:
            self.gasolina_actual-=1
            print(f"El vehiculo {self.tipo} con marca {self.marca} esta en marcha, conbustible restante: {self.gasolina_actual}")

            if self.gasolina_actual<0.1*self.gasolina:
                print(f"El {self.tipo} con marca {self.marca} esta a nivel de conbustible  bajo, ya que bajor a su capacidad debajo del 10%, conbustible restante {self.gasolina_actual}")

            if self.gasolina_actual==0:
                print(f'el vehiculo {self.tipo} con marca {self.marca} se ha detenido ya que la gasolina se acabo')
            


    def __str__(self):
        return f'el vehiculo es un tipo {self.tipo},con marca {self.marca} con tipo de conbustible {self.conbustible}'

class Moto(Vehiculo):
   def __init__(self,marca,conbustible,gasolina,gasolina_actual):
       super().__init__(marca,conbustible,gasolina,gasolina_actual)
       self.tipo= 'Moto'

class Carro(Vehiculo):
    def __init__(self,marca,conbustible,gasolina,gasolina_actual):
        super().__init__(marca,conbustible,gasolina,gasolina_actual)
        self.tipo='Carro'
        
moto=Moto('yamaha','corriente',30,15)
carro=Carro('chevrolet','Diesel',50,10)
print(moto)
print(carro)
print(type(moto))
print(type(carro))

moto.encender()
moto.marcha()


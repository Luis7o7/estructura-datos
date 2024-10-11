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
        if self.en_marcha:
            consumo_de_conbustible=0.1
            self.gasolina_actual=max(0,self.gasolina_actual-consumo_de_conbustible)
            print(f'el vehiculo{self.marca}esta en marcha. su nivel de conbustible actual es{self.gasolina_actual}')
            if self.gasolina_actual<= 0:
             print('el vehiculo se ha detenido, nivel de conbustible 0')
             self.en_marcha=False
            
        else:
            print('el vehiculo no esta en marcha')


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
        
moto=Moto('yamaha','corriente',30,0.5)
carro=Carro('chevrolet','Diesel',50,10)
print(moto)
print(carro)
moto.encender()
carro.encender()
moto.marcha()
carro.marcha()


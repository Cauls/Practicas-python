class Perro():
    def __init__(self, tipo, nombre, sexo, edad):
        self._tipo = tipo
        self._nombre = nombre
        self._sexo = sexo
        self._edad = edad
    
    def ladrar(self):
        print("Guau guau")
    
    def comer(self, comida):
        print(f"El perro {self._nombre} esta comiendo {comida}")
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    
    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, valor):
        self._sexo = valor
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        self._edad = valor

miPerro = Perro("Border Collie", "Joselito", "Macho", 5)
print(f"Tengo un {miPerro.tipo} que se llama {miPerro.nombre}")
miPerro.ladrar()
miPerro.comer("polla")
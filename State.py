
class State:
    def __init__(self, nombre, repeticiones):
        self._nombre = nombre
        self._repeticiones = repeticiones
        self._canales_siguientes = []
        self._canales_anteriores = []
        self._estados_siguientes = []
        self._estados_anteriores = []

#Puedes hacerme los get y set de esta clase

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_repeticiones(self):
        return self._repeticiones
    
    def set_repeticiones(self, nuevas_repeticiones):
        self._repeticiones = nuevas_repeticiones

    def get_canales_siguientes(self):
        return self._canales_siguientes
    
    def set_canales_siguientes(self, nuevos_canales_siguientes):
        self._canales_siguientes = nuevos_canales_siguientes

    def get_canales_anteriores(self):
        return self._canales_anteriores
    
    def set_canales_anteriores(self, nuevos_canales_anteriores):
        self._canales_anteriores = nuevos_canales_anteriores

    def get_estados_siguientes(self):
        return self._estados_siguientes
    
    def set_estados_siguientes(self, nuevos_estados_siguientes):
        self._estados_siguientes = nuevos_estados_siguientes

    def get_estados_anteriores(self):
        return self._estados_anteriores
    
    def set_estados_anteriores(self, nuevos_estados_anteriores):
        self._estados_anteriores = nuevos_estados_anteriores

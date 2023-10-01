class Auxi:
    def __init__(self, nombre, repeticiones):
        self._nombre = nombre
        self._repeticiones = repeticiones

    def __str__(self):
        return self._nombre + " " + str(self._repeticiones)

    # Método para obtener el valor de nombre
    def get_nombre(self):
        return self._nombre

    # Método para establecer el valor de nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Método para obtener el valor de repeticiones
    def get_repeticiones(self):
        return self._repeticiones

    # Método para establecer el valor de repeticiones
    def set_repeticiones(self, nuevas_repeticiones):
        self._repeticiones = nuevas_repeticiones

import Auxi as Auxi
import State as State


# Lista de entrada

def listar_estados(lista_entrada):
    repeticiones = []
    estados_unicos = set(lista_entrada)
    estados_unicos_lista = list(estados_unicos)

    for estado in estados_unicos_lista:
        repeticiones.append(lista_entrada.count(estado))
       
    return estados_unicos_lista , repeticiones


    


# Contar la frecuencia de cada estado en la lista
   # for estado in lista_entrada:
    #    estado.contar_repeticiones()
    

    print("Conteo de estados:")
    for estado, frecuencia in conteo_estados.items():
        print(f"Estado: {estado}, Frecuencia: {frecuencia}")


    print("Estados únicos:")
    for estado in estados_unicos_lista:
        print(estado)

    return estados_unicos_lista


def crear_Canales(lista_entrada):
    canales = {}
    for i, valor in enumerate(lista_entrada[0]):
        canal_nombre = f"canal_{chr(65 + i)}"  # Nombres de canal: canal_A, canal_B, canal_C, ...
        canales[canal_nombre] = []

    # Procesar cada valor en la lista de entrada
    for valor in lista_entrada:
        for i, estado in enumerate(valor):
            canal_nombre = f"canal_{chr(65 + i)}"  # Determinar el nombre del canal
            canales[canal_nombre].append(int(estado))
    
    for canal_nombre, valores in canales.items():
        print(f"{canal_nombre}: {valores}")

    return canales

lista_entrada = ["000", "101", "100", "011", "110", "101" ,"010","001","010", "101","111","000","111","001","110","011","101", "011","111","000","111","010","101","010","111","110","011","000","001","100"]

estado, rep = listar_estados(lista_entrada)

def crear_estados(estado, rep):
    lista_estados = []
    for i in range(len(estado)):
        lista_estados.append(State.State(estado[i], rep[i]))
    return lista_estados

lista_estados = crear_estados(estado, rep)

for estado in lista_estados:
    print(estado.get_nombre(), estado.get_repeticiones())

#crear_Canales(lista_entrada)


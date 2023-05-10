import pandas as pd

# Clase Enfermedades
class Enfermedades:
    def __init__(self, nombre, dicSint, count):
        self.nombre = nombre
        self.dicSint = dicSint
        self.count = count

# Diccionario de síntomas y valores
dicSint = {'fiebre': 2, 'dolor de cabeza': 4, 'falta de aire': 8, 'mareo': 16, 'dolor muscular': 24, 'tos': 48}

# Leer el archivo de Excel
data = pd.read_excel('ruta_del_archivo.xlsx')

# Crear una lista para almacenar los objetos de enfermedades
lista_enfermedades = []

# Iterar por cada fila del archivo de Excel
for index, row in data.iterrows():
    # Obtener el nombre de la enfermedad
    nombre = row['nombre']  # Asegúrate de que 'nombre' sea el nombre correcto de la columna en tu archivo

    # Calcular el valor de count sumando los valores de los síntomas activos
    count = sum(dicSint[sintoma] for sintoma, valor in dicSint.items() if row[sintoma] == 'si')

    # Crear un objeto Enfermedades y agregarlo a la lista
    enfermedad = Enfermedades(nombre, dicSint, count)
    lista_enfermedades.append(enfermedad)
print(lista_enfermedades)
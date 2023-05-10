import csv

"""
    Método que lee el archivo CSV que extrajo la información del EXCEL
    Retorna:
        dateSymptoms (Array de los síntomas) 
        dateDisease (Array de las enfermedades)
"""
def readCSV():
    with open('dates.csv', 'r') as f:
        dateSymptoms = []
        datesDisease=[]
        for line in f:
            words=line.split("\t")
            disease=[words[-1].strip()]
            symptoms=words[:-1]
            dateSymptoms.append(symptoms)
            datesDisease.append(disease)
        return dateSymptoms,datesDisease
dateSymptoms,dateDisease = readCSV()
print(dateSymptoms)

"""
    Método que convierte la lista de listas de 'Si' y 'No' en una matriz con
    valores binarios organizados
    Retorna: binaryList(Array de binarios como representación de booleano)
"""
def binary_converter(Array:list):
    tempList=[[1 if value=="Si" else 0 for value in subLista]for subLista in Array]
    binaryList=["".join(map(str, iterator)) for iterator in tempList]
    return binaryList
proof=binary_converter(dateSymptoms)

binaryList= binary_converter(dateSymptoms)
"""
    Método que toma la lista binaria y la convierte en numeros decimales a través de un ciclo FOR
    Retorna: decimalList (Array de decimales como representación de los números binarios)
"""
def decimal_converter(Array:list):
    decimalList= []
    for iterator in Array:
        decimalNumber= int(iterator,2)
        decimalList.append(decimalNumber)
    print(decimalList)
decimal_converter(proof)
    
def convert_dictionary(Array:list, Array2:list):
    dictDisiase = {}
    for keyDisease in Array:
        for valueSymptoms in Array2:
            dictDisiase[keyDisease]=valueSymptoms
            break
    print(dictDisiase)
        
convert_dictionary(dateDisease,dateSymptoms)
import csv
def readCSV():
   with open('dates.csv', 'r') as f:
        dates = []
        datesDisease=[]
        for line in f:
            words=line.split("\t")
            disease=[words[-1].strip()]
            symptoms=words[:-1]
            dates.append(symptoms)
            datesDisease.append(disease)
        return dates,datesDisease
array,disease = readCSV()
print(disease)
print(array)



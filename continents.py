import csv
path = r"F:/гугл загрузки/countries (2).csv"

def ReadCsvAndGenerateDict( func,path ):
    res = dict()
    with open(path,'r') as f:
        reader = csv.DictReader(f,delimiter=';')
        for r in reader:
            func(r,res)
    return res
    
def Task1(country:dict,res:dict):
    if res.get(country["Континент"]):
        res[country["Континент"]].append(country["Страна"])
    else:
        res[country["Континент"]] = [country["Страна"]]
        
def Task2(country:dict,res:dict):
    res[country["Континент"]] = res.get(country["Континент"],0) + int(country["Население_чел"] )

def Task3(country:dict,res:dict):
    res[country["Континент"]] = res.get(country["Континент"],0) + float(country["Площадь_квкм"].replace(",",".") )
    
def Task4(country:dict,res:dict):
    res[country["Континент"]] = res.get(country["Континент"],0) + float(country["Население_чел"].replace(",",".") )*(1/2)*(1/100)
    
result1 = ReadCsvAndGenerateDict(Task1,path)
result2 = ReadCsvAndGenerateDict(Task2,path)
result3 = ReadCsvAndGenerateDict(Task3,path)
res4 = ReadCsvAndGenerateDict(Task4,path)
a = [result1,result2,result3,res4]
for i in a:
    for el in i:
        c = 0
        while c <=10:
            print(el,end = " " )
            c+=1
        

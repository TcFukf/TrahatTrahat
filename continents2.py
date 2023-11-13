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
    res[country["Страна"]] = res.get(country["Страна"],
                                     0) + float( country["Население_чел"] )*(1.01)**3
    
res1 = ReadCsvAndGenerateDict(Task1,path)
s = sum(res1[i] for i in res1)
av = s/len(res1)
res2 = {k:v for k,v in res1.items() if v > av}
res3 = dict(sorted(res2.items(), key = lambda a : a[1],reverse = True)[:10] )

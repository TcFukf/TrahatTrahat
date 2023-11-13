import json
# 1 TASK
fname = "delete.txt"
with open(fname,"w") as file:
    print("   some \n string",file = file)
with open(fname) as f:
    for line in f.readlines():
        print(line.strip())
    
# 2 Task    
def writeArray(lines ,fname, mode = "a+"):
    with open(fname,mode) as file:
        print("\n".join(lines),file = file,end = "")
#3 Task
path = r"C:/Users/Валерий/Desktop/ЛАБЫ ИНФА/Lab10 Архив к лб_Файлы_main.zip"
from zipfile import ZipFile
import os 
#with ZipFile(path, "r") as myzip:
#    myzip.extractall("extracted/")
listDirs = []
for currentDir, _, files in os.walk("extracted"):
    #print(currentDir, _, files)
    for file in files:
        if file[-3:len(files):1] == ".py":
            listDirs.append(currentDir)
            break
listDirs.sort()
writeArray(listDirs,"OUTPUT.txt",mode = "w")

# 4 Task
""" 1) автор, 2) название, 3) год
издания, 4) город, где издана книга, 5) название издательства, 6) цена книги"""
books = []
for author in ["Aniya Enina", "Pelevin", "Roman Gelud"]:
    for name in ["KGBT+","Story about Alisher", "GenderFluid"]:
        for year in range(1994,2010,5):
            for city in ["Moscow","Dubai","Piter"]:
                for pub in ["1C","PLANETA"]:
                    for cost in range(222,444,111):
                        books.append( {"author":author,"name":name,"year":year,"city":city,"publishment":pub,"cost":cost} )
books = sorted(books[:100:10], key = lambda a : a["name"])
json_string = json.dumps(books)
with open("books.json","w") as f:
    json.dump(books,f)

# Task 5
import csv
with open("books.csv","w",newline = "") as f:
    writer = csv.DictWriter(f,fieldnames = books[0].keys(),delimiter=';')
    writer.writeheader()
    writer.writerows(books)
##    for row in books:
##        writer.writerow(row)
    

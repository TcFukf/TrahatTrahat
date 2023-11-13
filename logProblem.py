from pprint import pprint
import re

class SmallDataException(Exception):
    def __init__(self,text,size):
        self.text = text
        self.size = size

path = "logFile.txt"
fakePath = "logFile"
try:    
    with open(path) as f:
        text =  f.read()
    minSize = 6_000
    if len(text) < minSize:
        raise SmallDataException(f"length of text must be > {minSize}",len(text))
except FileNotFoundError as ex:
    print("File not founded")
    print(ex.args)
    #raise ex
    
except SyntaxError as ex:
    print(ex.args)

except SmallDataException  as ex:
    print(ex)
else:
    patt = r"\d+\.\d+\.\d+\.\d+"
    oldRes = []
    for i in re.findall(patt,text):
        if(i not in oldRes):
            oldRes.append(i)
    #print(oldRes)
    res = set(re.findall(patt,text) )
    print(*res,sep = "\n")

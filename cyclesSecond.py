import math
target = math.e
ValidDelta = 10**-5
n = 1
curRes = (1 + 1/n)**n
delta = target - curRes
while delta > ValidDelta:
    n+=1
    curRes = (1 + 1/n)**n
    delta = target - curRes
    #print(f"curRes:{curRes}, E:{target}, diff {delta}")
print(n)
    

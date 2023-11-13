#n = int (input("n":))
n = 5
spacesCount = 4
for i in range(1,n+1):
    line = ""
    for _ in range(spacesCount):
        line+=" "
    spacesCount-=1
    for sign in range(1,i+1):
        line+=str(sign)
    for sign in range(i-1,0,-1):
        line+=str(sign)
    print(line)

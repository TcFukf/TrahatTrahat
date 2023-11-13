import math


def FloatRange(st,end,step):
    while (st < end):
        yield st
        st+=step
def Y1(x):
    return ( 1+ (x**2)/(1+x**2) )**0.5;
def Y2(x):
    return 2*abs( math.cos(x) );

x=[i for i in FloatRange(-3,3,0.5)]

yl = [Y1(i) for i in x]
y2 = [Y2(i) for i in x]
filename = 'data.txt'
with open(filename, 'w') as outfile:
    outfile.write('# значения x , yl и y2\n')
    for xi, yi, yj in zip(x, yl,y2):
        print(f"{xi}, {yi}, {yj}",file = outfile)
        

y = list(map(lambda a, b: a+b, yl, y2))
y.sort(reverse = True)

with open(filename, 'a') as outfile:
    print('# Результат задания x и s',file = outfile)
    for xi, yi in zip(x, y):
        outfile.write(f'{xi}, {yi}\n')
    outfile.write(f"min(y) = {min(y)}")

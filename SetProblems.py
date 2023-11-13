
def isPrimary(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n = 15
# 2*k + 1 < n-10
#2*k < n-11
#k < (n-11)/2
#k >= (n-11)/2
A = set ( a for a in range(n-10,n+10) if a%2==1 )
B = set ( a for a in range(n,n+10+1) if isPrimary(a) )
union = A.union(B)
inter = A.intersection(B)
div1 = A-B
div2 = B-A
sim = B.symmetric_difference(A)
print(f"A:{A}\nB:{B}")
print(union,inter,div1,div2,sim,sep="\n")

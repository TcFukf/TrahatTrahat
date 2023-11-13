"""Дано слово-образец. В заданном списке слов (не более 100) определить слова, в которых
нет хотя бы одной буквы из слова-образца. Выведите такие слова, а также буквы, которых
нет в слове-образце"""
listWords = ["poko", "hitler","my", "fight"]
patternWord = "phko"
pattern = set(patternWord)
result = []
for word in listWords:
    for sign in word:
        if (sign not in pattern): # нет хотя бы одной буквы из слова-образца
            result.append(word)
            break
print(result)

import numpy
#numpy.roots([1, 9, 21, -1, -30])
U = {-5,-4,-3,-2,-1,1,2,3,4,5}
A = {-2, 1, 5}
a,b,y,g = -6,1,24,-20
B = set(int(i) for i in numpy.roots([1, a, b, y ,g]))
print(f"A:{A}")
print(f"B:{B}")
print(f"U:{U}")

print( A.union(B))

print( A.intersection(B))

print(A-B)

print(B-A)
print(A.symmetric_difference(B))
print( U - B ) # ne B tipo
C = ( A.symmetric_difference(B).symmetric_difference(A) )

print(f"C:{C}")
# БУЛЕВОе множ
import itertools
multiplicity = A.union(B)
boolean = set()
for r in range(len(multiplicity)+1) :
        temp = set(itertools.combinations(multiplicity, r))
        for i in temp :
            boolean.add(i)
print(boolean)
print(len(boolean))


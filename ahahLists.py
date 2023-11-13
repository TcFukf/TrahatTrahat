import random
impo
# Создайте список с числовыми элементами, целыми, положительными, из диапазона [0;a], n штук.
#Необходимо вывести в новый список все элементы, удовлетворяющие условию по варианту.
A = 11 #  a in condition
n = 11 # same
ar = [random.randint(0,A) for _ in range(n)]
# 3.	элементы с чётных индексов
newAr = [ar[ind] for ind  in range(len(ar)) if ind%2==0]
print(ar,newAr,sep = "\n")

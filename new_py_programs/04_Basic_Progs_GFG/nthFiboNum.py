from math import sqrt

def fibo_find(n):
    fibo_num = (((1+sqrt(5))**n) - ((1-sqrt(5))**n))/((2**n)*(sqrt(5)))
   
    return print(fibo_num)

fibo_find(52)
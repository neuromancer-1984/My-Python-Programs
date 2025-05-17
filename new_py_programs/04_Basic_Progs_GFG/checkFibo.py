import math
def Fibo(n):
    num1 = (5*(n**2))+4
    num2 = (5*(n**2))-4
    sq1 = math.sqrt(num1)
    sq2 = math.sqrt(num2)

    if (int(sq1))**2 == num1 or (int(sq2))**2 == num2:
        return True
    elif (int(sq1))**2 == num1 and (int(sq2))**2 == num2:
        return True
    else:
        return False
    
    
# Fibo(31)

for i in range(1, 100):
    if(Fibo(i)==True):
        print(f"{i} ,is a Fibonacci number")
    else:
        print(f"{i} ,NOT a Fibonacci number")
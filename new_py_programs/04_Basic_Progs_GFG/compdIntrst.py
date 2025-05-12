def compIntrst(P, R, t):
    x = 1 + R/100
    y = x**t
    Amount =  P * y
    CI = Amount - P
    print('Compound Interest: ',CI)

compIntrst(10000, 10.25, 5)
    
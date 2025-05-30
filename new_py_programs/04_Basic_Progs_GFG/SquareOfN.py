def sqNum(n):
    sum = 0
    for i in range(1, n+1):
        sq1 = i**2
        sum += sq1

    print('Sum of squares is: ',sum)


sqNum(5)
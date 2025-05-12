# def break_num(num):
#     count=0
#     while(num!=0):
#         count += 1
#         num = num // 10
    
#     return count

# def digit(num):
#     i=0
#     while(num!=0):
#         i = num % 10
#         print(i)
#         num = num // 10
    
# digit(56)


def Armstrong(num):
    n1 = num
    count=0
    while(n1!=0):
        count += 1
        n1 = n1 // 10
    n2 = num
    i=0
    sum=0
    while(n2!=0):
        i = n2 % 10
        p = i**count
        sum += p
        n2 = n2 // 10

    if(sum==num):
        print(f'{num} : is an Armstrong Number')
    else:
        print(f'{num} : is NOT an Armstrong Number')
  
Armstrong(163)  
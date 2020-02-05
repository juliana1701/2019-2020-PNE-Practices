
def fibo(n):
    index1 = 0
    index2 = 1
    sumn = 0
    for number in range(0, n+1):
        if number == 0:
            sumn = 0
        elif number == 1:
            sumn = 1
        else:
            sumn = index1 + index2
            index1 = index2
            index2 = sumn
    return sumn


print("The 5th term of the fibonacci series is:", fibo(5))
print("The 10th term of the fibonacci series is:", fibo(10))
print("The 15th term of the fibonacci series is:", fibo(15))

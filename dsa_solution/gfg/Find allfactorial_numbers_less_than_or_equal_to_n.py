def factorialNumbers(n):
    fact = 1
    i = 1
    while fact <= n:
        fact = fact * i
        print(fact, end=" ")
        i += 1


a = 3
cc = factorialNumbers(a)

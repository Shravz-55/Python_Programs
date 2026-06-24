#WAP to Find Factorial of a Given Number

def factorial_num(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))
print(factorial_num(n))
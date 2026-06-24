#WAP to Generate Fibonacci Series

def fib(n):
    n1 = 0
    n2 = 1

    for i in range(n):
        print(n1, end=" ")

        n3 = n1 + n2
        n1 = n2
        n2 = n3

n = int(input("Enter value: "))
fib(n)
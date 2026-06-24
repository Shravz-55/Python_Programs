#WAP to Find Sum of Individual Digits

def sumdigit(n):
    total = 0

    while n > 0:
        val = n % 10
        total += val
        n = n // 10

    return total

n = int(input("Enter a number: "))
print(sumdigit(n))
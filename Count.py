#WAP to Count the Number of Digits Present in a Given Number

def count_digits(n):
    if n == 0:
        return 1

    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count

n = int(input("Enter a number: "))
print(count_digits(n))
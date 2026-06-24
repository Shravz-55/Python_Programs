#WAP to Check Whether the Given Number is Prime Number or Not
def prime_number(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        return "Prime Number"
    else:
        return "Not a Prime Number"

n = int(input("Enter a number: "))
print(prime_number(n))
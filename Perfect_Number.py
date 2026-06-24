#WAP to Check Whether the Given Number is Perfect Number or Not

def perfect_num(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n:
        return "Perfect Number"
    else:
        return "Not a Perfect Number"

n = int(input("Enter a value: "))
print(perfect_num(n))
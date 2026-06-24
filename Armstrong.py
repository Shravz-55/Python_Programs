#WAP to Check Whether the Given Number is Armstrong Number or Not

def armstrong(n):
    s = 0
    temp = n
    digits = len(str(n))

    while temp > 0:
        ld = temp % 10
        s = s + ld ** digits
        temp = temp // 10

    if s == n:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"

n = int(input("Enter a value: "))
print(armstrong(n))
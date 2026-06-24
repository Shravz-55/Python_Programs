#WAP to Reverse the Number

def rev_num(n):
    rev = 0

    while n > 0:
        ld = n % 10
        rev = rev * 10 + ld
        n = n // 10

    return rev

n = int(input("Enter a number: "))
print(rev_num(n))
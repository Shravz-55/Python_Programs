#WAP to Find Product of Individual Digits

def product_digit(n):
    product = 1

    while n > 0:
        ld = n % 10
        product *= ld
        n = n // 10

    return product

n = int(input("Enter a number: "))
print(product_digit(n))
#WAP to Convert Decimal to Binary

def decimal_to_binary(n):
    return bin(n)[2:]

num = int(input("Enter a decimal number: "))
print(decimal_to_binary(num))
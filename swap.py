#WAP to Swap Two Numbers Using Temporary Variable

def swap(a, b):
    temp = a
    a = b
    b = temp

    return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = swap(a, b)

print("After swapping:")
print(a, b)
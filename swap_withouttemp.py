#WAP to Swap Two Numbers Without Using Temporary Variable

def swap(a, b):
    a, b = b, a
    return a, b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

x, y = swap(x, y)

print("After swapping:")
print(x, y)
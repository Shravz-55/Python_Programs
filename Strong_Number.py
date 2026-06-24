#WAP to Check Whether the Given Number is Strong Number or Not

def strong_num(n):
    total = 0

    for i in str(n):
        fact = 1

        for j in range(1, int(i) + 1):
            fact = fact * j

        total = total + fact

    if total == n:
        return "Strong Number"
    else:
        return "Not a Strong Number"

n = int(input("Enter a value: "))
print(strong_num(n))
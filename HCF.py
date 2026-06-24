#WAP to Find HCF/GCD of Two Numbers

def hcf_of_two_no(n1, n2):
    hcf = 1

    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            hcf = i

    return hcf

n1 = int(input("Enter first value: "))
n2 = int(input("Enter second value: "))

print(hcf_of_two_no(n1, n2))
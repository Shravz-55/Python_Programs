#WAP to Find LCM of Two Numbers

def lcm_num(n1, n2):
    max_num = max(n1, n2)

    while True:
        if max_num % n1 == 0 and max_num % n2 == 0:
            return max_num

        max_num += 1

n1 = int(input("Enter first value: "))
n2 = int(input("Enter second value: "))

print(lcm_num(n1, n2))
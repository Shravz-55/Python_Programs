#WAP to Print Prime Numbers Between 2 to 10

def prime_num():
    for i in range(2, 11):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2:
            print(i, end=" ")

prime_num()
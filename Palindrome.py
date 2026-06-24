#

def palindrome(n):
    rev = 0
    temp = n

    while temp > 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10

    if n == rev:
        return "Palindrome"
    else:
        return "Not a Palindrome"

n = int(input("Enter a value: "))
print(palindrome(n))
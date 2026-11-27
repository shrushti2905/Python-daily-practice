# Find sum of digits using function

def digit_sum(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    return total

print(digit_sum(4567))
# Check perfect number

def perfect_number(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n

print(perfect_number(28))
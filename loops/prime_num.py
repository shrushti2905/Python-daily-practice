# Q5. Check whether a given number is prime or not.

number = 29
is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
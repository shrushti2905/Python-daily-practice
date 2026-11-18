# Q3. Reverse a given number using a while loop.

number = 12345
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse:", reverse)
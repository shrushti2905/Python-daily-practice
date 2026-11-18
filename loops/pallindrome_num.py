# Q4. Check whether a given number is a palindrome or not.

number = 121
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
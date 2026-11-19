# Handle an error when converting invalid text into an integer.

value = "hello"

try:
    number = int(value)
    print(number)
except ValueError:
    print("Invalid number format")
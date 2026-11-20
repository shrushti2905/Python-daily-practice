# Handle an error when accessing an invalid list index.

numbers = [10, 20, 30, 40]

try:
    print(numbers[5])
except IndexError:
    print("Index does not exist")
# Use else to display a message when no exception occurs.

a = 50
b = 10

try:
    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division successful")
    print("Result:", result)
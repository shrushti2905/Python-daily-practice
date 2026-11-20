# Handle both division by zero and invalid number conversion errors.

values = ["10", "0", "hello"]

try:
    a = int(values[0])
    b = int(values[2])
    print(a / b)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Please provide valid numbers")
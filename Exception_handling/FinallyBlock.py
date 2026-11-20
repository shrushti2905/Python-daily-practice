# Use finally to execute a message whether an exception occurs or not.

try:
    number = 100 / 5
    print("Result:", number)

except ZeroDivisionError:
    print("Invalid division")

finally:
    print("Program execution completed")
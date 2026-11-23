# Find the missing number in a list containing numbers from 1 to N.

def missing_number(arr, n):
    for i in range(1, n+1):
        if i not in arr:
            return i

print(missing_number([1, 2, 4, 5], 5))
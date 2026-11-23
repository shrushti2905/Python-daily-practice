# Find the average of elements in a list.

def average(arr):
    total = 0

    for num in arr:
        total += num

    return total / len(arr)

print(average([10, 20, 30, 40]))
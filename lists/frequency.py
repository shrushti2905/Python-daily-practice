# Count the frequency of each element in a list.

def frequency(arr):
    result = {}

    for num in arr:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

    return result

print(frequency([1, 2, 2, 3, 3, 3]))
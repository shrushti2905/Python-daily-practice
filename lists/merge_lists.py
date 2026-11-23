# Merge two lists into one list.

def merge_lists(arr1, arr2):
    result = []

    for num in arr1:
        result.append(num)

    for num in arr2:
        result.append(num)

    return result

print(merge_lists([1, 2, 3], [4, 5, 6]))
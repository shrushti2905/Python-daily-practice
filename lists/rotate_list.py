# Rotate a list to the right by K positions.

def rotate_list(arr, k):
    if len(arr) == 0:
        return arr

    k = k % len(arr)

    for i in range(k):
        num = arr.pop()
        arr.insert(0, num)

    return arr

print(rotate_list([1, 2, 3, 4, 5], 2))
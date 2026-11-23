def move_zeros(arr):
    result = []

    for num in arr:
        if num != 0:
            result.append(num)

    for num in arr:
        if num == 0:
            result.append(num)

    return result

print(move_zeros([0, 1, 0, 3, 12]))
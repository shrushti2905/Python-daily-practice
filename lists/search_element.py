# Search for an element in a list.

def search_element(arr, target):
    for num in arr:
        if num == target:
            return True

    return False

print(search_element([10, 20, 30, 40], 30))
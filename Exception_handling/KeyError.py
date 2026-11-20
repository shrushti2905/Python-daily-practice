# Handle an error when accessing a dictionary key that does not exist.

student = {
    "name": "Riya",
    "age": 21,
    "course": "MCA"
}

try:
    print(student["marks"])
except KeyError:
    print("Key not found in dictionary")
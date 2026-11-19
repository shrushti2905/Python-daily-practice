# Reverse a string without using slicing.

text = "Python"
reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)
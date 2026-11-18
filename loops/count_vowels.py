# Q1. Count the total number of vowels in a given string.

text = "Python Programming"
count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels:", count)
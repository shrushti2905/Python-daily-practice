# Count the total number of words in a sentence without using split().

sentence = "Python is easy to learn"
count = 0
inside_word = False

for ch in sentence:
    if ch != " " and not inside_word:
        count += 1
        inside_word = True
    elif ch == " ":
        inside_word = False

print("Total words:", count)
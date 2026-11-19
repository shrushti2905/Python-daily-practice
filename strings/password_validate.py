# Check whether a password has at least 8 characters and contains a digit.

password = "python123"
has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True
        break

if len(password) >= 8 and has_digit:
    print("Valid password")
else:
    print("Invalid password")
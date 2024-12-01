def isPhoneNumber(text):
    if len(text) != 12:  # Check if the length is exactly 12
        return False
    for i in range(0, 3):  # Check first 3 characters are digits
        if not text[i].isdecimal():
            return False
    if text[3] != '-':  # Check for the first dash
        return False
    for i in range(4, 7):  # Check next 3 characters are digits
        if not text[i].isdecimal():
            return False
    if text[7] != '-':  # Check for the second dash
        return False
    for i in range(8, 12):  # Check last 4 characters are digits
        if not text[i].isdecimal():
            return False
    return True  # All conditions are satisfied

def getUserInput():
    user_input = input("Enter a phone number (format: XXX-XXX-XXXX): ")
    if isPhoneNumber(user_input):
        print(f"The input {user_input} is a valid phone number.")
    else:
        print(f"The input {user_input} is not a valid phone number.")

# Call the input function
getUserInput()

message = 'Call me at 415-515-1011 tommorow, 414-515-1011 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: "+ chunk)

print("Done")

# gets integer shift from user
def get_shift():
    while True:
        try:
            return int(input("Enter shift: "))
        except:
            continue

# returns given char shifted by shift
def shift_char(char, shift):
    # if no shift or char not alpha, return char
    if (shift == 0 or char.isalpha() is False):
        return char
    # if positive shift
    elif (shift > 0):
        newchar = ord(char)
        for i in range(0, shift):
            # Z or z
            if (newchar == 90 or newchar == 122):
                newchar -= 25
            else:
                newchar += 1
        return chr(newchar)
    # if negative shift
    elif (shift < 0):
        newchar = ord(char)
        for i in range(shift, 0):
            # A or a
            if (newchar == 65 or newchar == 97):
                newchar += 25
            else:
                newchar -= 1
        return chr(newchar)

message = input("Enter message: ")
shift = get_shift()

output = ""

for char in message:
    output += shift_char(char, shift)

print(output)

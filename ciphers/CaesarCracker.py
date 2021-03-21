# shifts given char by shift
def shift_char(char, shift):
    # if no shift or char not alpha, return char
    if (shift == 0 or char.isalpha() is False):
        return char

    # ensure positive shift
    while (shift < 0):
        shift += 26

    # get new char    
    newchar = ord(char)
    for i in range(0, shift):
        # Z or z
        if (newchar == 90 or newchar == 122):
            newchar -= 25
        else:
            newchar += 1
    return chr(newchar)

# shifts given string by shift
def shift_string(string, shift):
    output = ""
    # shift string char by char
    for char in string:
        output += shift_char(char, shift)
    return output

# returns score of given string based on common words
def get_score(string):
    score = 0
    words = string.split()
    # increment score if word in common
    for word in words:
        if (word.lower() in common):
            score += 1
    return score

# get user message and clean message
message = input("Enter message to decode:\n")
cleanmessage = ""
for char in message:
    if (char.isalpha() or char == ' '):
        cleanmessage += char.lower()

# get common words list
f = open("../CommonWords.txt", "r")
common = f.read().lower().splitlines()
f.close()

# collect scores for all shifts
hitlist = []
for i in range(0, 26):
    shifted = shift_string(cleanmessage, i)
    score = get_score(shifted)
    hitlist.append(score)

# get best shift and print results
bestshift = hitlist.index(max(hitlist))
certainty = int((max(hitlist) / len(cleanmessage.split())) * 100)
result = shift_string(message, bestshift)
print()
print("Best shift found: " + str(bestshift))
print("Certainty: " + str(certainty) + "%")
print()
print(result)

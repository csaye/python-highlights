# returns whether given char is vowel
def is_vowel(ch):
    lower_ch = ch.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    return lower_ch in vowels

# returns given word converted to pig latin
def platin(word):
    # if empty
    if len(word) == 0: return ''
    # if first character vowel
    if is_vowel(word[0]): return word + 'yay'
    # if one char
    if len(word) == 1: return word + 'ay'
    # if greater than one char
    return word[1:] + word[0] + 'ay'

# get string and words
string = input('Enter a string to convert to pig latin: ')
words = string.split()
# convert words and string
p_words = [platin(word) for word in words]
p_string = ' '.join(p_words)
# print converted string
print(p_string)

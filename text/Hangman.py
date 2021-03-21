import random

MIN_LENGTH = 5

def get_rand_word(): # returns a random word from the given text file
    lines = open("./CommonWords.txt").read().splitlines()
    word = random.choice(lines)
    while (len(word) < MIN_LENGTH):
        word = random.choice(lines)
    return word

def put_char(word, char, pos): # puts given char at given position in given word
    return word[:pos] + char + word[(pos + 1):]

RAND_WORD = get_rand_word() # get random word from file
WORD_LENGTH = len(RAND_WORD) # get random length of word

wrong_letters = "" # initialize wrong letters
guessed_letters = "" # initialize guessed letters
for i in range(0, len(RAND_WORD)):
    guessed_letters += "_"

print("Guess characters in the " + str(WORD_LENGTH) + " letter string. !giveup to give up.\n")

while (True):
    guess = input("Guess: ") # get user guess
    if (guess == "!giveup"): # if give up command, break
        print("Gave up after " + str(len(wrong_letters)) + " wrong guesses.")
        print("The string was \"" + RAND_WORD + "\".")
        break
    for i in range(0, len(guess)): # for each char in string guess
        #tries += 1 # increment tries
        if guess[i] not in RAND_WORD: # if guess not in word
            if guess[i] not in wrong_letters: # if guess not already in wrong letters
                wrong_letters += guess[i] # add guess to wrong letters
            continue
        for j in range(0, WORD_LENGTH): # for each char in random word
            if (guess[i] == RAND_WORD[j]): # if guess is at correct position in word
                guessed_letters = put_char(guessed_letters, RAND_WORD[j], j) # add to guessed letters
    print(guessed_letters) # print guessed letters
    print("no: " + wrong_letters + "\n") # print wrong letters
    if (guessed_letters == RAND_WORD): # if all letters guessed, break
        print("You guessed the string with " + str(len(wrong_letters)) + " wrong guesses.")
        break

import random

UNDERSCORE_MODE = True

def get_rand_word():
    lines = open("CommonWords.txt").read().splitlines()
    return random.choice(lines)

RAND_WORD = get_rand_word()
WORD_LENGTH = len(RAND_WORD)

print("Guess the random " + str(WORD_LENGTH) + " character string. !giveup to give up.")

tries = 0
while (True):
    guess = input("Guess: ")
    if (guess == "!giveup"):
        print("Gave up after " + str(tries) + " tries.")
        print("The string was \"" + RAND_WORD + "\".")
        break
    if (len(guess) != WORD_LENGTH):
        print("Guess must be " + str(WORD_LENGTH) + " characters.")
        continue
    tries += 1
    if (guess == RAND_WORD):
        print("You guessed the string in " + str(tries) + " tries.")
        break
    if (UNDERSCORE_MODE):
        underscores = ""
        for i in range(0, WORD_LENGTH):
            if (guess[i] == RAND_WORD[i]):
                underscores += RAND_WORD[i]
            else:
                underscores += "_"
        print(underscores)
    else:
        correct = 0
        for i in range(0, WORD_LENGTH):
            if (guess[i] == RAND_WORD[i]):
                correct += 1
        print("Guess had " + str(correct) + " correct characters.")

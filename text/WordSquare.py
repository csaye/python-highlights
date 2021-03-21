import random

# globals
size = 4
max_unknowns = 0
runs = 100
lines = open('./CommonWords.txt').read().splitlines()
words = [word for word in lines if len(word) == size]

# main
for run in range(runs):
    
    # initialize square
    square = []
    for y in range(size):
        row = []
        for x in range(size):
            row.append('?')
        square.append(row)

    # get shuffled words of proper length
    random.shuffle(words)

    # for each word
    for x in range(size):
        # for each word in words
        for word in words:
            chars = square[x]
            fail = False
            # check random word in square
            for c in range(size):
                if chars[c] == '?': continue
                elif chars[c] != word[c]: fail = True
            # if word meets specifications
            if not fail:
                # add to square and break
                for y in range(size):
                    square[x][y] = word[y]
                    square[y][x] = word[y]
                break

    # count unknowns
    unknowns = 0
    for row in range(size):
        for col in range(size):
            # count unknowns
            if square[row][col] == '?': unknowns += 1
    # skip if more than max
    if unknowns > max_unknowns: continue

    # print square
    for row in range(size):
        word = ''.join(square[row])
        print(word)
    print('-')
    print('unknowns: ' + str(unknowns))
    if run != runs - 1: print()

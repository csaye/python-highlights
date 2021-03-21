def similarity_score(str_a, str_b):
    score = 0
    short = min(len(str_a), len(str_b))
    for i in range(0, short):
        if (str_a[i] == str_b[i]):
            score += 1
        if (str_a[len(str_a) - 1 - i] == str_b[len(str_b) - 1 - i]):
            score += 1
    return score

common = open("./CommonWords.txt").read().splitlines()

input_word = input("Enter word: ")

if input_word in common:
    print("Word \"" + input_word + "\" is correct.")
else:
    max_score = -1
    best_words = []
    for word in common:
        score = similarity_score(input_word, word)
        if score > max_score:
            max_score = score
            best_words = [word]
        elif score == max_score:
            best_words.append(word)
    print("Did you mean \"" + "\", \"".join(best_words) + "\"?")
    certainty = int((max_score / (2 * len(input_word))) * 100)
    print("Certainty: " + str(certainty) + "%")

from words import valids
from words import game_words
from words import easy
from analysis1 import findMatches

removeIndices = []


class bcolors:
    # https://stackoverflow.com/a/287944
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def removeYellows(
    yellows, wordlist
):  # check if a yellow is NOT in the word, then remove
    index = 0
    removeIndices = []
    for word in wordlist:
        for letter in yellows:
            if letter not in word:
                # remove word from wordlist
                # wordlist.pop(index)
                removeIndices.insert(0, index)
                break
        # print(removeIndices)
        index += 1
    wordlist = removeAllIndices(removeIndices, wordlist)
    return wordlist


def removeYellows2(
    yellows, wordlist
):  # check if there's a yellow would've been green, then remove
    index = 0
    removeIndices = []
    for word in wordlist:
        for y in yellows:
            if word[y[1]] == y[0]:
                removeIndices.insert(0, index)
                break
        index += 1
    wordlist = removeAllIndices(removeIndices, wordlist)
    return wordlist


def removeGrays(
    grays, wordlist
):  # check if a gray exists in the word at all, then remove
    index = 0
    removeIndices = []
    for word in wordlist:
        for letter in grays:
            if letter in word:
                # print("popping ",index)
                # wordlist.pop(index)
                removeIndices.insert(0, index)
                break
        index += 1
    # print(removeIndices)
    wordlist = removeAllIndices(removeIndices, wordlist)
    return wordlist


def removeGreens(greens, wordlist):  # check if a green isn't where it should be
    index = 0
    removeIndices = []
    for word in wordlist:
        for g in greens:
            if word[g[1]] != g[0]:
                removeIndices.insert(0, index)
                break
        index += 1
    wordlist = removeAllIndices(removeIndices, wordlist)
    return wordlist


def removeAllIndices(removeIndices, wordlist):
    for index in removeIndices:
        wordlist.pop(index)
    return wordlist


tester = ["lathe", "bathe", "later", "hater", "magni"]
tester2 = ["lathe", "bathe", "later", "hater", "magni"]

options = game_words

guaranteedLetters = []
suggestion = "soare"
while len(options) > 1:
    print(
        f"Enter word guess (Hint: try using {bcolors.OKCYAN}{suggestion}{bcolors.ENDC})"
    )
    word_guess = input()

    print("Enter result (e = empty, g = green, y = yellow)")
    result = input()

    #pre processing loop to populate guaranteedLetters
    #protects against case where a green letter is further in the word than a gray
    i = 0
    for letter in result:
        if letter == 'g':
            guaranteedLetters += word_guess[i]
        i += 1

    i = 0
    for letter in result:
        if letter == "e":
            if word_guess[i] not in guaranteedLetters:
                options = removeGrays([word_guess[i]], options)
                print("removing grays for ", letter, " and ", word_guess[i])
        elif letter == "y":
            guaranteedLetters += word_guess[i]
            options = removeYellows([word_guess[i]], options)
            options = removeYellows2([[word_guess[i], i]], options)
        elif letter == "g":
            guaranteedLetters += word_guess[i]
            options = removeGreens([[word_guess[i], i]], options)
        i += 1
    if len(options) == 0:
        print("Something went wrong")
    if len(options) > 1:
        suggestion = findMatches(options, options)[0][1]
        print(options)
    elif len(options) == 1:
        print(f"{bcolors.OKGREEN}{options[0]}{bcolors.ENDC}")

# print(realtest)

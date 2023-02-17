from words import valids
from words import game_words
from words import easy

tester = ["basic", "prams", "starn", "shark", "shard"]
# print(valids[745])
# print(game_words[342])


def average(num_list):
    return sum(num_list) / len(num_list)


def inCommon(word1, word2):  # word2 is the reference word
    total = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            total += 3
        elif word1[i] in word2:
            total += 1

    return total


def findClosest(searcher, word_list):
    max = [0, "xxxxx"]
    for word in word_list:
        if word != searcher:
            if inCommon(word, searcher) > max[0]:
                max[0] = inCommon(word, searcher)
                max[1] = word
    print(max)


def buildDict(searcher, word_list):
    myDict = {}
    for word in word_list:
        if word != searcher:
            myDict[word] = inCommon(word, searcher)
    return myDict


def calcAverage(searcher, word_list):
    match_values = []
    for word in word_list:
        if word != searcher:
            match_values.append(inCommon(word, searcher))
    return average(match_values)


def findMatches(word_list_source, word_list_reference):
    averages = []
    for word in word_list_source:
        temp = calcAverage(word, word_list_reference)
        averages.append([temp, word])
    averages.sort(reverse=True)
    return averages


if __name__ == "__main__":
    temp = findMatches(valids, game_words)
    print(temp[:10])


# print(calcAverage("prams",valids))
# findClosest("basic",game_words)

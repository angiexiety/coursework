#analyse 3 speeches for characters, sentences, words, unique words, % unique words, longest words with output into txt file for frequency of words

import collections
import os #jk i realized how to save it into the py folder

def readFile(fileName):
    """
    opens and reads a .txt file
    """
    inFile = open(fileName, "r")
    fileContentsList = inFile.read()
    inFile.close()
    return fileContentsList

def cleanText(text):
    """
    1) replaces lines, hyphens, double spaces with single space
    2) converts upper case to lower case
    3) removes all non-alphabetic characters other than space
    """
    cleanString = " "
    cleanText = text.replace("\n", " ")
    cleanText2 = cleanText.replace("-", " ")
    for aChar in cleanText2:
        if aChar.isalpha() or aChar == " ":
            cleanString = cleanString + aChar
    lowercaseText = cleanString.lower()
    while lowercaseText.count("  ") > 0:
        finalText = lowercaseText.replace("  ", " ")
    return finalText


def splitText(string):
    """
    splits text into a list (space for delimitation)
    """
    wordList = []
    wordList = string.split(" ")
    return wordList


def sortedList(wordList):
    """
    sorts alphabetically
    """
    filteredList = filter(None, wordList)
    sortedList = sorted(filteredList)
    return sortedList


def uniqueWords(wordList):
    """
    sorts alphabetically to unique words
    """
    uniqueWords = set(wordList)
    sortedUniqueWords = sorted(uniqueWords)
    return sortedUniqueWords


def numberCharacters(stuffInFile):
    """
    all the characters used in the text
    """
    characterList = list(stuffInFile)
    return characterList


def numberSentences(stuffInFile):
    """
    number of sentences used in the text (by counting end punctuation symbols)
    """
    period = stuffInFile.count(".")
    exclamationMark = stuffInFile.count("!")
    questionMark = stuffInFile.count("?")
    numberSentences = period + exclamationMark + questionMark
    return numberSentences


def uniqueWordPercentage(uniqueWordList, cleanedTextAsList):
    """
    percentage of unique words (unique divided by total)
    """
    lengthUniqueWords = len(uniqueWordList)
    lengthAllWords = len(cleanedTextAsList)
    percentOfUnique = lengthUniqueWords / lengthAllWords * 100
    return percentOfUnique


def longestWord(uniqueWordList):
    """
    longest word
    """
    longestWord = max(uniqueWordList, key=len)
    return longestWord


def dictionaryList(cleanedTextAsList, uniqueWordList):
    """
    stores each unique word and frequency
    """
    dictionary = {}
    for aVal in uniqueWordList:
        lineDict = {aVal: (cleanedTextAsList.count(aVal))}
        dictionary.update(lineDict)
    return dictionary


def writeDictionary(fileName, fileContents):
    """
    contents of dictionary list into new .txt file
    """
    outFile = open(fileName, "w")
    sortedDict = sorted(fileContents.items())
    for key, value in sortedDict:
        outFile.write(str(key) + " " + str(value) + "\n")
    outFile.close()


def mostUsedWords(dictionary):
    """
    10 most frequent words over 5 letters
    """
    fiveplusDict = {}
    for key, value in dictionary.items():
        if len(key) > 5:
            fiveplusDict[key] = value
    topTenWords = sorted(fiveplusDict.items(), key=lambda item: -item[1])[:10]
    return topTenWords


def main():
    allSpeeches = ("PMHarperBerlinWall.txt", "PresObamaBerlinSpeech.txt", "PresObamaInauguralAddress.txt")
    speechName = ("Harper's Berlin Speech: ", "Obama's Berlin Speech: ", "Obama's Inaugural Address: ")
    speechDict = ("PMHarperBerlinWallDict.txt", "PresObamaBerlinSpeechDict.txt", "PresObamaInauguralAddressDict.txt")
    for i in range(3):
        try:
            stuffInFile = readFile(allSpeeches[i])
        except ValueError:
            print("supplied file does not contain text!")
        except IOError:
            print("the file cannot be opened!")
            return

        cleanedString = cleanText(stuffInFile)
        textAsString = splitText(cleanedString)
        cleanedTextAsList = sortedList(textAsString)
        uniqueWordList = uniqueWords(cleanedTextAsList)
        dictionary = dictionaryList(cleanedTextAsList, uniqueWordList)

        numOfCharacters = numberCharacters(stuffInFile)
        numOfSentences = numberSentences(stuffInFile)
        percentUnique = uniqueWordPercentage(uniqueWordList, cleanedTextAsList)
        longWord = longestWord(uniqueWordList)
        dictFile = writeDictionary(speechDict[i], dictionary)
        wordsUsedMost = mostUsedWords(dictionary)

        print("\n" + speechName[i])
        print(str(len(numOfCharacters)) + " characters")
        print(str(numOfSentences) + " sentences")
        print(str(len(cleanedTextAsList)) + " words")
        print(str(len(uniqueWordList)) + " unique words")
        print("{0:2.1f}% of words are unique".format(percentUnique))
        print("the longest word is: " + longWord)
        print("\nmost used words over 5 letters are: ")
        for word, number in wordsUsedMost:
            print(str(word) + ": " + str(number) + " times")
        print("~" * 20)


main()
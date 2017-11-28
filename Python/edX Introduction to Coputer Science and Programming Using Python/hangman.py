# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = loadWords()

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    isGuessed = True
    wordLetters = list(secretWord)
    for letter in wordLetters:
        if not (letter in lettersGuessed):
            isGuessed = False
    
    return isGuessed

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    wordLetters = list(secretWord)
    for letter in wordLetters:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += '_ '
    
    return guessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        allLetters.remove(letter)
        
    return ''.join(allLetters)
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    wordLength = len(secretWord)

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(wordLength) + " letters long.")
    print("------------")

    wordGuessed = False
    guessesLeft = 8
    guessed = []
    lettersLeft = string.ascii_lowercase

    while wordGuessed == False and guessesLeft > 0:
        print("You have " + str(guessesLeft) + " guesses left.")
        print("Available letters: " + lettersLeft)
        guess = input("Please guess a letter: ").lower()
        if guess in guessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guessed))
            print("------------")
        elif not guess in list(secretWord):
            guessed.append(guess)
            guessesLeft -= 1
            lettersLeft = getAvailableLetters(guessed)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, guessed))
            print("------------")
        else:
            guessed.append(guess)
            lettersLeft = getAvailableLetters(guessed)
            print("Good guess: " + getGuessedWord(secretWord, guessed))
            print("------------")

        wordGuessed = isWordGuessed(secretWord, guessed)

    if wordGuessed:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses, the word is " + secretWord + ".")

# Play the game
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

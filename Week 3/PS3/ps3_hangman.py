# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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
    print(str(len(wordlist)) + " words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    WordGuessed = True
    for i in range(len(secretWord)):
        letter_found = 0
        for j in range(len(lettersGuessed)):
            if secretWord[i]==lettersGuessed[j]:
                letter_found=1
                break
        if letter_found == 0:
            WordGuessed = False
            break
    
    return WordGuessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    WordNow = ""
    for i in range(len(secretWord)):
        letter_found = 0
        for j in range(len(lettersGuessed)):
            if secretWord[i]==lettersGuessed[j]:
                WordNow += secretWord[i]                
                letter_found=1
                break
        if letter_found == 0:
            WordNow +="_ "
            
    return WordNow


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ""
    
    for i in range(len(lettersGuessed)):
        j=0        
        while j < len(all_letters):
            if lettersGuessed[i]!=all_letters[j]:
                available_letters += all_letters[j]
            j+=1
        all_letters = available_letters
        available_letters = ""
            
    return all_letters
    

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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print("-----------")
    
    lettersGuessed = []
    guesses = 8    
    WordGuessed = False

    #print(secretWord)

    while guesses>0 and WordGuessed == False:
        print("You have " + str(guesses) + " guesses left.")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter: ")
        
        test1=0
        for i in range(len(lettersGuessed)):
            if letter == lettersGuessed[i]:
                test1 = 1
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                break       
        if test1==0:
            for i in range(len(secretWord)):
                if letter==secretWord[i]:
                    lettersGuessed.append(letter)
                    test1 = 2
                    print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                    break
        if test1==0:
             print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
             guesses-=1
        if test1 != 2:        
            lettersGuessed.append(letter)
        
        print("-----------")
        WordGuessed = isWordGuessed(secretWord, lettersGuessed)
        
    if WordGuessed == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was else. ")
    
        
index = random.randint(0,len(wordlist)-1)
secretWord = wordlist[index]
secretWord = "c"
hangman(secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

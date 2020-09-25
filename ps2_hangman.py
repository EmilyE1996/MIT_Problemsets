# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME,"r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()


res = "y"
while res == "y":
    word = choose_word(wordlist)
    tempWord = word
    ##print(word)
    word2 = list()
    for i in range(0, len(word)):
        word2.append("_ ")
    ##print("list is ", word2)
    ##print("length of list is ", len(word2))
    alphabet = str("abcdefghijklmnopqrstuvwxyz")
    numGuesses = 8

        

    print("Welcome to the game, Hangman!\nI am thinking of a word that is ", str(len(word)), "letters long.\n----------------\nYou have", str(numGuesses), "guesses left.\nAvailable letters: ", alphabet)

    while str("_ ") in word2:
        letter = input("Please guess a letter: ")
        letter = str.lower(letter)

        ###if letter has been guessed previously
        
        if letter not in alphabet:
            print("Invalid guess; please guess something you've not already guessed.")
            continue

        ### If letter is in word

        if letter in tempWord:
            j = tempWord.find(letter)
            while letter in tempWord:
                tempWord = tempWord.replace(letter, " ", 1)
                word2[j] = letter
                j = tempWord.find(letter)

            alphabet = alphabet.replace(letter, "")
            print("Good Guess: ", *word2, sep="")
            if numGuesses > 1:
                print("Remaining Letters: ", alphabet, "\nYou have ", str(numGuesses), " guesses left.\n----------------------")
            else:
                print("Remaining Letters: ", alphabet, "\nYou have ", str(numGuesses), " guess left.\n----------------------")
            
            
        ### if letter not in word
            
        else:
            if numGuesses < 2:
                print("Sorry, you lose! The word was ", word)
                break
            else:
                numGuesses = numGuesses -1
                alphabet = alphabet.replace(letter, "")
                
                print("Oops! That letter is not in the word.\nCurrent Guess: ", *word2, sep="")
                if numGuesses > 1:
                    print("Remaining Letters: ", alphabet, "\nYou have ", str(numGuesses), " guesses left.\n----------------------")
                else:
                    print("Remaining Letters: ", alphabet, "\nYou have ", str(numGuesses), " guess left.\n----------------------")

    if str("_ ") not in word2:
        print("Congratulations! You've guessed the word: ", word)
    res = input("Do you want to continue? Y or N: ")
    res = str.lower(res)

    

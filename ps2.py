# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:46:33 2024

@author: marcs
"""
import time
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
     return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    if list(secret_word) == letters_guessed:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    result = ""
    for i in secret_word:
        if i in letters_guessed:
            result += i.upper()
        else:
            result += "_ "
    return result


def get_available_letters(letters_guessed):
   all_letters = string.ascii_lowercase
   list_letters = list(all_letters)
   for i in all_letters:
       if i in letters_guessed:
           list_letters.remove(i)
   letters = "".join(list_letters)
   return letters
    
    
def hangman(secret_word):
    
    guesses = 6
    warning = 0
    number_letters=len(secret_word)
    letters_guessed = []
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {number_letters} long.")
    print("----------")
    
    while not is_word_guessed(secret_word,letters_guessed) and guesses > 0:
        time.sleep(3)
        print(f"You have {guesses} guesses left.")
        available_letters = get_available_letters(letters_guessed)
        print(f"Available letters: {available_letters}")
        
        letter = input("Please guess a letter:").lower()
        
        if letter in letters_guessed:
            print("You already guessed that letter, try again.")
            print(get_guessed_word(secret_word, letters_guessed))
            print("----------")
            continue
        
        letters_guessed += letter
        
        if str.isalpha(letter) == False:
            print("That's not an alphabetic character. Try again.")
            print(get_guessed_word(secret_word, letters_guessed))
            warning += 1
            if warning == 3:
                warning = 0
                guesses -= 1
                print("You introduced incorrect characters 3 times, sorry but it cost you a guess!")
            print("----------")
            continue
        
        if letter in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}")
            print("----------")
           
        
        if letter not in secret_word:
            print(f"Oops that letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}")
            guesses -= 1
            print("----------")
        

    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you guessed the word! Cheers!")
    else:
        print(f"Game over, sorry! The word was {secret_word.upper()}")



wordlist = load_words()
word = choose_word(wordlist)
print(word)    
        
hangman(word)

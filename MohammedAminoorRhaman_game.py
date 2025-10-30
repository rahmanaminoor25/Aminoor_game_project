#Establishing list of words which contain only 6 characters and imports

with open("words_alpha.txt","r") as file:
    word_list = [i for i in file]

word_list = [i for i in word_list if len(i)==6]
 
import random
#-------------------------------------------------------------------------------------
 #user inputs
print("Wordle!")
print("Can you guess the word? you have upto 6 attempts to guess correctly!")
attempts = 1
computer_pick = str(random.choices(word_list)[0])

while attempts > 0:
    try:
        guess1 = str(input("Type your guess:"))
        if guess1==computer_pick:
            print("You guessed correctly! well done!")
        else:
            print("Not quite")
            attempts-=1
            print('\nYou have', attempts, 'attempts left')
        
    except:
        print("Please enter a word with 6 characters")


#Establishing list of words which contain only 6 characters and imports

with open("words_alpha.txt","r") as file:
    word_list = [i for i in file]

word_list = [i for i in word_list if len(i)==6]
 
import random

#-------------------------------------------------------------------------------------
#defining functions
#___________________

#colour_code function
#--------------------
def colour_code(x,y):
    '''The colour code function colour codes each letter to black, yellow or green. x is the guess
    word, y is the target word chosen by the computer'''

    #discritzing/seperating each character in a list
    x2 = [i for i in x.lower()]
    y2 = [i for i in y.lower()]

    #initialises each character as being black
    feedback = ['black']*len(y2)

    #defines which character has been used up (Important when dealing with duplicate characters)
    used_char = [False]*len(x2) 


    '''This for loop checks for any 'greens'. If greens are found (i.e if the user 
    has correctly found the correct letter in its correct position wrt to the 
    actual word), that character position is classifed as being used.'''
    for i in range(len(y2)):
        if y2[i]== x2[i]:
            feedback[i]='green'
            used_char[i] = True

    '''This checks for any yellows. If there are duplicate letters (e.g. user tries a word
    with two 'l's and the actual word only contains one 'l'), this loops ensures that
    characters will only become yellow if there is a matching character AND if the character
    has not been used up by the previous for loop that checks for values that need to be coded
    as green'''
    for i in range(len(y2)):
        if feedback[i] =='black':
            for j in range(len(x2)):
                if not used_char[j]  and  y2[i] == x2[j]:
                    feedback[i]='yellow'
               
                break 

    #printing the letters based on what colours they should be
    for i in range(len(y2)):
        if feedback[i]=='green':
            print(f"{colour_green}{y2[i]}{colour_end}", end='|')
        elif feedback[i]=='yellow':
            print(f"{colour_yellow}{y2[i]}{colour_end}", end='|')
        else:
            print(f"{y2[i]}", end='|')

 #------------------------------------------------------------------------------------------      

        

#-------------------------------------------------------------------------------------
 #user inputs
print("Wordle!")
print("Can you guess the word? you have upto 6 attempts to guess correctly!")
attempts = 6
computer_pick = str(random.choices(word_list)[0])
#computer_pick_disc = [i for i in computer_pick.lower()]

while attempts > 0:
    try:
        guess = str(input("Type your guess:"))
        guess_disc = [i for i in guess.lower()] #seperated/discreatized the characters in a list
        if guess==computer_pick:
            print("You guessed correctly! well done!")
            for i in range(len(guess_disc)):
                print(f"{colour_green}{guess_disc[i]}{colour_end}", end='|')
        else:   
            attempts-=1
            print('\nYou have', attempts, 'attempts left')
            colour_code(computer_pick,guess)


        
    except:
        print("Please enter a word with 5 characters")


#Establishing list of words which contain only 6 characters and imports


'''this file contains all the words that have been used for wordle, and will constitute
the word bank from which the computer chooses from '''
with open("filtered-wordle-words.csv","r") as file:
    word_list = [i.strip().lower() for i in file]

#this word file contains a large dictionary of words.
with open("words_alpha.txt","r") as file2:
    word_list2 = [i.strip().lower() for i in file2]

word_list_total = [i for i in word_list2 if len(i)==5]

 
import random

#-------------------------------------------------------------------------------------
#defining functions
#___________________

#colour_code function
#--------------------
def colour_code(x,y):
    '''The colour code function colour codes each letter to black, yellow or green.
    x is the GUESS word.
    y is the TARGET (actual) word chosen by the computer.'''

    #discritzing/seperating each character in a list
    x2 = [i for i in x.lower()] # Guess list
    y2 = [i for i in y.lower()] # Target list

    #initialises each character as being black
    feedback = ['black']*len(x2) # Feedback is for the guess

    #defines which character has been used up (Important when dealing with duplicate characters)
    used_char = [False]*len(y2) # Used_char is for the target

    #defining the colours 
    colour_green = '\033[92m'  # Green
    colour_yellow = '\033[93m' # Yellow
    colour_end = '\033[0m'     # Reset color back to default

    '''This for loop checks for any 'greens'. If greens are found (i.e if the user 
    has correctly found the correct letter in its correct position wrt to the 
    actual word), that character position is classifed as being used.'''
    for i in range(len(x2)):
        # Assumes guess and target are the same length
        if i < len(y2) and x2[i] == y2[i]:
            feedback[i]='green'
            used_char[i] = True

    '''This checks for any yellows. If there are duplicate letters (e.g. user tries a word
    with two 'l's and the actual word only contains one 'l'), this loops ensures that
    characters will only become yellow if there is a matching character AND if the character
    has not been used up by the previous for loop that checks for values that need to be coded
    as green'''
    for i in range(len(x2)):
        if feedback[i] =='black':
            for j in range(len(y2)):
                if not used_char[j]  and  x2[i] == y2[j]:
                    feedback[i]='yellow'
                    used_char[j] = True
                    break 

    #printing the letters based on what colours they should be
    for i in range(len(x2)):
        if feedback[i]=='green':
            print(f"{colour_green}{x2[i]}{colour_end}", end='|')
        elif feedback[i]=='yellow':
            print(f"{colour_yellow}{x2[i]}{colour_end}", end='|')
        else:
            print(f"{x2[i]}", end='|')

    print() # Adds a newline after the guess is printed

 #------------------------------------------------------------------------------------------      

        

#-------------------------------------------------------------------------------------
#defining the colours 
colour_green = '\033[92m'  # Green
colour_yellow = '\033[93m' # Yellow
colour_end = '\033[0m'     # Reset color back to default

#user inputs/game
print("Wordle!")
print("Can you guess the word? you have upto 6 attempts to guess correctly!")

#difficulty code block
n = 0
while n<1:
    difficulty = str(input("choose difficulty for game (easy/normal/hard):")).lower()
    if difficulty =='easy':
       attempts = 8
       n+=1
    elif difficulty=='normal':
       attempts = 6
       n+=1
    else:
       print("please enter either 'easy','normal' or 'hard")



computer_pick = str(random.choices(word_list)[0])
#print(computer_pick)
#computer_pick_disc = [i for i in computer_pick.lower()]

while attempts > 0:
        guess = str(input("Type your guess:")).lower().strip()

        #seperated/discreatized the characters in a list
        guess_disc = [i for i in guess.lower()] 
        
        #count number of attempts used
        attempt_count = 0

        '''this verifies the user enters a 5 lettered word that is found in our dictionary.
        Dictionary contains over 15,000 words'''  
        if guess not in word_list_total:
            print ('Please enter a 5 lettered word that exists')
        else:
            #if user enters correct word
            if guess==computer_pick:
                print("You guessed correctly! well done!")
                for i in range(len(guess_disc)):
                    print(f"{colour_green}{guess_disc[i]}{colour_end}", end='|')
                print()
                score = 1
                attempts_used = attempt_count + 1
                print("You used %d attempts"%(attempts_used) )
                break       
            else:
                #user enters incorrect word
                attempts-=1
                attempt_count+=1
                #print('\nYou have', attempts, 'attempts left')
                colour_code(guess,computer_pick)


if attempts == 0:
    print("better luck next time! the word was:",computer_pick)
    losses = 1

        
    





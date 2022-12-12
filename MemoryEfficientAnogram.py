# !!! PLEASE READ THE README FILE IN ROOT DIRECTORY BEFORE RUNNING !!!

# This program will take an input of two words and determine if the two words
# are an anorgram or not. The program can also recognize if the string contains
# whitespace or not. It can be used with either the default test data, or take 
# words from user input. 

# This program utilizes the best Python programming practices by taking an 
# Object Oriented approach and using the all() function to limit the amount of 
#times the interpriter will have to loop through characters in the given string. 
#This results in a memory effecient program. 

# Written by Justin Schadwill


class DetermineAnogram:
    def __init__(self, anogram_list):
        self.anogram_list = anogram_list

    def determine_anogram(self):
        for i in self.anogram_list:
            anogram = None
            white_space = None
            word1, word2 = i, self.anogram_list[i]

            # Check if either word contains a space
            if ' ' in word1 or ' ' in word2:
                white_space = True

            # Check if each character in word1 is in word2
            anogram = all(char in word2 for char in word1)

            # Print the result
            print(word1, word2, end='')
            if anogram:
                print(' - anogram', end='')
            else:
                print(' - not an anogram', end='')
            if white_space:
                print(' with white space')
            else:
                print('')


def read_from_sample():
    anogram_list = {
        'hello': 'jello',
        'below': 'elbow',
        'study': 'dusty',
        'night': 'thing',
        'act': 'cat',
        'goop': 'droop',
        'dessert': 'stressed',
        'bad credit': 'debit card',
        'gainly': 'laying',
        'conversation': 'voice rants on',
        'eleven plus two': 'twelve plus one',
        'pie': 'shoe',
        'they see': 'the eyes',
        'funeral': 'real fun',
            }

    anogram_check = DetermineAnogram(anogram_list)
    anogram_check.determine_anogram()
    

def read_from_user_input():
    while True:
        anogram_list = {'a': 'b'} 
        word1 = input('Enter first word: ')
        word2 = input('Enter second word: ')
        anogram_list[word1] = word2
        anogram_list.pop('a')
        
        anogram_check = DetermineAnogram(anogram_list)
        anogram_check.determine_anogram()


# Program starts here
selection = input('\nChoose your method:\nRead from sample data: (1)\nRead from user input: (2)\n')
try:
    if int(selection) == 1:
        read_from_sample()
    elif int(selection) == 2:
        read_from_user_input()
    else:
        print('Invalid selection. Please run the program again.')

except ValueError:
    print('ValueError. Please run the program again.')
    exit()


# Basic Word Jumble WITH Levels
#
# Dustin Hammack
# March 31, 2017

# This will be the very basic, but full version of "Word Jumble"

"""

    THE MOST RECENT VERSION AS OF April 1st

    AND FULLY WORKING WITH LEVELS AND HINTS

"""

# IMPORTS
import random
import hints_dictionary
from hints_dictionary import HINTS


# Initialize Global Variables & Constants

#CONSTANTS - Word tuples for each level ( Used SORTED to alphabatize tuples)
WORDS_1 = ('begin', 'belt', 'cable', 'chair', 'chew', 'choir',
          'code', 'cook', 'draw', 'easy', 'empty', 'flair',
          'floor', 'flurt', 'food', 'game', 'glass', 'golf',
          'grab', 'grasp', 'grind', 'group', 'grow', 'grown',
          'head', 'light', 'limit', 'list', 'math', 'music',
          'nose', 'radio', 'ring', 'shoe', 'song', 'table',
          'take', 'third', 'tuba', 'watch', 'wear', 'wire',
          'worth', 'wrap', 'write', 'wrong', 'yard'
          )

WORDS_2 = ('answer', 'arrow', 'bounce', 'break', 'chart', 'cheek',
          'chili', 'coding', 'combat', 'crawl', 'create', 'drain',
          'export', 'first', 'found', 'glove', 'heard', 'heater',
          'hired', 'import', 'jumble', 'laptop', 'march', 'noise',
          'phone', 'photo', 'praise', 'prayer', 'python', 'random',
          'robot', 'season', 'smart', 'smile', 'strike', 'string',
          'strong', 'switch', 'tennis', 'window', 'worker', 'worry'
          )
          
WORDS_3 = ('banana', 'bionic', 'blanket', 'boxing', 'bright',
          'broken', 'charter', 'cheese', 'complex', 'delete',
          'distort', 'doctor', 'edition', 'fiction', 'finger',
          'foster', 'friend', 'future', 'gaming', 'global',
          'guitar', 'island', 'length', 'master', 'method',
          'mirror', 'module', 'muffin', 'musical', 'notepad',
          'occupy', 'online', 'option', 'peanut', 'pillow',
          'printer', 'program', 'remove', 'reverse', 'setting',
          'sprawl', 'stairs', 'tablet', 'wallet', 'washer',
          'welcome'
          )
          
WORDS_4 = ('absolute', 'advanced', 'approval', 'baseball', 'beginner',
          'biology', 'birthday', 'biscuit', 'bouncing', 'bowling',
          'british', 'calendar', 'cemetary', 'clarinet', 'computer',
          'constant', 'creating', 'download', 'dramatic', 'dresser',
          'dynamite', 'english', 'football', 'formula', 'fortune',
          'function', 'holiday', 'internet', 'keyboard', 'notebook',
          'nuclear', 'obscure', 'opponent', 'porkchop', 'progress',
          'property', 'prosper', 'robotics', 'russian', 'sequence',
          'spectrum', 'storage', 'template', 'traverse', 'triangle',
          'trumpet', 'universe', 'variable', 'various', 'vehicle',
          'wrestler'
          )

WORDS_5 = ('calculator', 'cassette', 'chairman', 'characters', 'commercial',
          'conditioner', 'counterpart', 'dictionary', 'difficult', 'discovery',
          'everlasting', 'everything', 'excellent', 'extraordinary', 'fireworks',
          'gathering', 'generation', 'information', 'inspection', 'instruction',
          'intermediate', 'introduction', 'knockout', 'manageable', 'mathematics',
          'merchandise', 'microfiber', 'microwave', 'motorcycle', 'newspaper',
          'orientation', 'parameter', 'preposition', 'programming', 'punctuation',
          'refrigerator', 'saxophone', 'skateboard', 'specifically', 'stonewall',
          'surrender', 'television', 'theasaurus', 'thermostat', 'tolerance',
          'ukrainian', 'universal', 'vocabulary', 'wilderness', 'xylophone'
          )
#GLOBAL variables
user_points = 0
tries = 3
level = 1

# Display the Instructions
def display_instructions():
    print("""
            Here is the classic word jumble game, where the computer will scramble a random word, and you
            the human will have to try and unscramble the word. You will get 10 points for each word you
            unscramble, and if you get stuck you can ask for a hint. Be careful though, it cost 10 points to
            ask for a hint, so round 1, you'll be on your own starting with no points. You have 3 chances to
            guess, otherwise you lose!

            (Hints cost 10 points, and you will not receive points for guessed word, when given hint.)

            DO YOU HAVE WHAT IT TAKES PUNY HUMAN?
          """)

# Jumble the chosen word
def jumble_word(word):
    jumble = ''
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print('\nThe jumble is: ', jumble)
    return word, jumble

# Take the user input
def user_input(word):
    global user_points
    global tries
    user_guess = input('\nYour guess: ')
    guess = user_guess.lower()
    #While user still has tries left, run this block
    while tries >= 1:
        if guess == 'hint':
                if user_points <= 0:
                    print('I\'m sorry, you do not have enough points for that.')
                    user_guess = input('\nYour guess (Remember hints cost 10 points): ')
                    guess = user_guess.lower()
                else:
                    print()
                    print('THE WORD HINT IS:\n ')
                    print('\t', HINTS[word]) #hints_dictionary.
                    user_points -= 10
                    user_guess = input('\nYour guess: ')
                    guess = user_guess.lower()
        elif guess != word or guess == '':
            tries -= 1
            if tries == 0:
                print('I\'m sorry, you didn\'t figure it out in time.')
                print(input('\n\nPress enter to quit game'))
                return
            print('\nSorry, that was not it.')
            print(tries)
            user_guess = input('\nYour guess (Remember hints cost 10 points): ')
            guess = user_guess.lower()           
        elif guess == word:
                print('\n\n\tCorrect!')
                print('\tThe word was \t\t', word)
                user_points += 10
                print('\n\n\nYou have ', user_points, 'points\n\n')
                tries = 3
                #print(tries)
                return user_points, tries
         
    if tries == 0:
        print('I\'m sorry, you didn\'t figure it out in time.')
        print(input('\n\nPress enter to quit game'))
        play_again()

#Ask user to play again
def play_again():
    global user_points
    global tries
    tries = 3
    another_play = input('\n\tWould you like to play again? (Y/N) ')
    again = another_play.lower()
    while again not in ('y', 'n'):
        while again == '':
            another_play = input('\n\tWould you like to play again? (Y/N) ')
            again = another_play.lower()
            if again == 'y':
                tries = 3
                level()
            elif again == 'n':
                return
        if again != ('y', 'n'):
            another_play = input('\n\tWould you like to play again? (Y/N) ')
            again = another_play.lower()
    if again == 'y':
        level()
    elif again == 'n':
        return

# Create the main function of the game
def main(word_list):
    word = random.choice(word_list)
    jumble_word(word)
    user_input(word)

#Define level function to call main function
def level():
    while user_points < 50:
        if user_points == 0:
            print('Welcome to level 1')
        main(WORDS_1)
    while user_points >= 50 and user_points < 100:      ####change code to 50 <= user_points < 100:
        if user_points == 50:
            print('Getting better, have a try at level 2')
        main(WORDS_2)
    while user_points >= 100 and user_points < 150:     ####change code to 50 <= user_points < 100:
        if user_points == 100:
            print('Now your just getting lucky. Try your luck on level 3')
        main(WORDS_3)
    while user_points >= 150 and user_points < 200:     ####change code to 50 <= user_points < 100:
        if user_points == 150:
            print('How can this be possible! There\'s no way you\'re passing level 4!')
        main(WORDS_4)
    while user_points >= 200 and user_points < 250:     ####change code to 50 <= user_points < 100:
        if user_points == 200:
            print('Are you sure you\'re not a computer? Here is the final level')
        main(WORDS_5)
        print('Congratulations, you can spell')
    play_again()

#Call functions and START game
display_instructions()
level()

#End game
print(input('\n\nPress enter to quit game'))

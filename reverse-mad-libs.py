# Reverse Mad Lib Project


# Attempting to clean up code by removing strings from functions
game_text = ["Dang, I wasn't expecting that answer. Try again!",
            "You did it! Feel free to play again.",
            "Looks like you're not in the mood, until next time!",
            "I can't use that response. Try again please!",
            "That's all the chances you get! Game over.",
            "How difficult should the game be? easy, medium, or hard? "]

def right(txt, srch_var, answer, blank_num, chances):
    """
    This function helps iterate to the next blank if the user gets the
    blank right.
    """
    txt = txt.replace(srch_var, answer)
    blank_num += 1
    chances = 3
    return (txt, blank_num, chances)


def fill_blanks(txt, bank):
    """
    This function will process the user's answers and return whether or 
    not they got it correct or incorrect. 
    """
    blank_num = 1
    chances = 3
    while blank_num <= 4:
        srch_var = '__' + str(blank_num) + '__'
        print(txt)
        answer = input('What should go in blank number ' + srch_var + '? ')
        if answer == bank[blank_num-1]:
            (txt, blank_num, chances) = right(txt, srch_var, answer, blank_num, chances)
        else:
            chances -= 1
            if chances == 0:
                return game_text[4]
            print(game_text[0])
    return game_text[1]                        

easy_txt = """
__1__ are tools that only execute instructions that they are explicitly 
given, making them inherently 'dumb'. When replacing a number or other piece 
of information with a placeholder, this placeholder is known as a __2__. 
The process of replacing a piece of information with a variable is known as 
an __3__. Finally, a __4__ is known as a piece of text that is surrounded on 
either side by quotation marks.
Word Bank: variable, computers, string, assignment
"""

easy_bank = ['computers', 'variable', 'assignment', 'string']

med_txt = """
A __1__ is a block of reusable code that performs a single, related action. 
A function operates by taking __2__ and transforming it in to the desired 
output. One of the most common operations is an __3__ satement; this operation 
can compare both numbers and strings by using conditional expressions like 
greater than and less than. Another common operation is using a __4__ loop.
A while loop will run until the defined condition is met."
Word Bank: if, function, input, while
"""

med_bank = ['function','input','if','while']

hard_txt = """
A while loop and if statement operate based on whether the 
following expression is 'True' or 'False', this is known as __1__ logic.
There is another loop statement known as a __2__ loop, this loop iterates 
through every value of the input whether it be a list of numbers or strings. 
The ability to change the identity of a variable or items in a list is known 
as __3__. The process of assigning the same item to multiple variables is 
known as __4__.
Word Bank: for, aliasing, mutability, boolean
"""

hard_bank = ['boolean', 'for', 'mutability', 'aliasing']

def chosen_text(lvl_choice):
    """
    Sets up the game based on the difficulty level chosen and then moves 
    into the blank filling portion of the game.
    """
    if lvl_choice == 'easy':
        txt = easy_txt
        bank = easy_bank
    elif lvl_choice == 'medium':
        txt = med_txt
        bank = med_bank
    elif lvl_choice == 'hard':
        txt = hard_txt
        bank = hard_bank
    print(fill_blanks(txt, bank))

startup = """Time to chill and play a game.

                 You only get 3 tries overall
                 All questions should be answered with lower case letters
                 """
                
def difficulty():
    """
    This function is meant to present the user with an opening prompt that 
    lets them select the difficulty of the mad lib game.
    """     
    print(startup)
    tries = 3
    level = ["easy", "medium", "hard"]
    lvl_choice = input(game_text[5])
    while lvl_choice not in level: 
        tries = tries - 1
        if tries == 0:
                return game_text[2]
        print(game_text[3])
        lvl_choice = input(game_text[5])
        if lvl_choice in level:
            continue
    return chosen_text(lvl_choice)
        
difficulty()

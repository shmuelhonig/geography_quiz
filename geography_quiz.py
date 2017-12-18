#!/usr/bin/env python2.7

easy_question = """The capital of France is ___1___\nThe capital of the \
United Kingdom is ___2___\nThe capital of Italy is ___3___\nAll three \
countries are located in ___4___, one of the seven continents"""
medium_question = """The largest state in the United States by population is \
___1___\nThe capital of ___1___ is ___2___\nThe smallest state by population \
is Wyoming, and the next smallest state is ___3___\nThe capital of ___3___ is \
___4___\nThe capital of ___5___, also known as The Natural State, is ___6___"""
hard_question = """___1___, the oldest state capital city in the United \
States, was founded in 1610\nThe largest state capital by population is \
___2___\n___3___ is the name of the largest city in two different states, but \
does not identify the capital of either\nAlthough Homer will never tell you \
the location of his home town, a real city with the same name is the capital \
of ___4___"""


easy_answers = {
    '___1___': 'PARIS',
    '___2___': 'LONDON',
    '___3___': 'ROME',
    '___4___': 'EUROPE'
    }

medium_answers = {
    '___1___': 'CALIFORNIA',
    '___2___': 'SACRAMENTO',
    '___3___': 'VERMONT',
    '___4___': 'MONTPELIER',
    '___5___': 'ARKANSAS',
    '___6___': 'LITTLE ROCK'
    }

hard_answers = {
    '___1___': 'SANTA FE',
    '___2___': 'PHOENIX',
    '___3___': 'PORTLAND',
    '___4___': 'ILLINOIS'
    }

updated_question = ''  # Refers to the specified question with completed blanks
# filled in.


def fill_it_in(key, value, which_question, blanks_completed):
    """
    Behavior: Fills in blanks when either user has answered correctly or has
    run out of guesses.
    : Parameters: The question chosen by the user, the current blank number,
    and the answer that should replace the blank. Also uses two global
    variables, one that keeps track of the number of blanks that have been
    completed and one that keeps track of the updated question, i.e. the
    question with appropriate blanks already filled in.
    : Return: The given question with relevant blanks filled in.
    """
    global updated_question
    if blanks_completed == 0:
        # When the first blank in the question is filled, the original question
        # must be updated.
        # When subsequent blanks are filled, the updated question must be
        # updated; therefore when the number of blanks completed is greater
        # than 0, the formula is different.
        # I tried multiple ways of achieving the same result with just one
        # reassignment statement (including converting the strings to lists),
        # and I found that this method was the easiest and cleanest way to do
        # it.
        updated_question = which_question.replace(key, value)
    else:
        updated_question = updated_question.replace(
            key, value)
    print "\n" + updated_question
    return updated_question


def you_are_incorrect(key, value, which_question, blanks_completed, num_attempts, correct_answers):
    """
    Behavior: For wrong answers, tells user how many attempts are left; if
    there are no more attempts, then it directs the program to go to the
    function that fills in the blank, and if there are more attempts, then it
    prompts the user to give another answer. If the user is correct this time,
    then it directs the program to go to the function that fills in the blank,
    and it also updates the number of blanks that have been answered correctly.
    If the user is incorrect again then the behavior repeats.
    : Parameters: The question chosen by the user, the current blank number,
    and the correct answer for the given blank. Also uses three global
    variables, one that keeps track of the number of blanks that have been
    completed, one that keeps track of the number of blanks that have been
    answered correctly, and one that stores the number of attempts the user has
    chosen to get.
    : Return: None (directs the program to other function).
    """
    attempts_taken = 1
    while attempts_taken < num_attempts:
        print '\nThat is incorrect. You have ' + str(
            num_attempts - attempts_taken) + ' attempts remaining\n'
        user_answer = raw_input(
            'What should be substituted for ' + key + '? ').upper()
        if user_answer == value:
            print '\nCorrect!'
            correct_answers = correct_answers + 1
            fill_it_in(key, value, which_question, blanks_completed)
            break
        attempts_taken = attempts_taken + 1
    if attempts_taken == num_attempts:
        print '\nThat is incorrect. You have no more attempts'
        fill_it_in(key, value, which_question, blanks_completed)


def play_quiz(which_dictionary, which_question, num_attempts):
    """
    Behavior: Initiates the quiz. Prompts user to fill in the blank, and,
    depending on whether the answer is correct or incorrect, directs the
    program to the appropriate function. If the user is correct, it updates
    the number of blanks that have been answered correctly. Before looping to
    the next blank to be filled in, updates the number of blanks that have been
    completed. Upon completion of game, lets user know how many questions they
    answered correctly and directs the program to the function that asks
    whether the user wants to play again.
    : Parameters: The question chosen by the user and the dictionary containing
    the appropriate answers. Also uses two global variables, one that keeps
    track of the number of blanks that have been completed and one that keeps
    track of the number of blanks that have been answered correctly.
    : Return: None (directs the program to other functions and prints some
    messages).
    """
    blanks_completed = 0 # Tracks how many blanks have been completed up to
    # that point during play
    correct_answers = 0 # Tracks how many blanks have been correctly answered
    # by the user
    for key, value in sorted(which_dictionary.iteritems()):
        user_answer = raw_input(
            '\nWhat should be substituted for ' + key + '? ').upper()
        if user_answer == value:
            print '\nCorrect!'
            correct_answers = correct_answers + 1
            fill_it_in(key, value, which_question, blanks_completed)
        else:
            you_are_incorrect(key, value, which_question, blanks_completed, num_attempts, correct_answers)
        blanks_completed = blanks_completed + 1
    print '\nThanks for playing! You answered ' + str(correct_answers) +\
          ' out of ' + str(len(which_dictionary)) + ' correctly'
    again()


def attempts():
    """
    Behavior: Collects user input for how many guesses user should get for each
    question. Prompts user again if invalid selection is made.
    : Parameters: None.
    : Return: The number of guesses chosen by the user.
    """
    while True:
        try:
            num_guesses = int(raw_input(
                'How many guesses would you like for each question? (5 max) '))
            if 5 >= num_guesses >= 1:
                break
            else:
                print '\nInvalid selection\n'
        except:
            print '\nInvalid selection\n'
    return num_guesses


def level():
    """
    Behavior: Collects user input for which level of quiz to play. Prompts user
    again if invalid selection is made.
    : Parameters: None.
    : Return: The level selected by the user.
    """
    print '\nThere are three levels: easy, medium, and hard.'
    level_options = ['EASY', 'MEDIUM', 'HARD']
    chosen_level = raw_input('Type your preference and press enter ').upper()
    while chosen_level not in level_options:
        print '\nInvalid selection.\n'
        chosen_level = raw_input(
            'Type your preference and press enter ').upper()
    return chosen_level


def question_allocation():
    """
    Behavior: Allocates the apprpriate question and dictionary to be used in
    the quiz based on user input.
    : Parameters: The level selected by the user.
    : Return: Prints the appropriate question and directs program to function
    for playing quiz.
    """
    selected_level = level()
    if selected_level == 'EASY':
        question = easy_question
        answers_dictionary = easy_answers
    if selected_level == 'MEDIUM':
        question = medium_question
        answers_dictionary = medium_answers
    if selected_level == 'HARD':
        question = hard_question
        answers_dictionary = hard_answers
    num_attempts = attempts()
    print '\n' + question
    play_quiz(answers_dictionary, question, num_attempts)


def again():
    """
    Behavior: Asks user if user wants to play again. If user selects yes, then
    it directs program to once again go to function that asks user for required
    input. Prompts user again if invalid selection is made.
    : Parameters: None.
    : Return: None (directs program to another function).
    """
    play_again = raw_input(
        '\nWould you like to play again? Type yes or no ').upper()
    play_again_options = ['YES', 'NO']
    while play_again not in play_again_options:
        print '\nInvalid selection.\n'
        play_again = raw_input(
            '\nWould you like to play again? Type yes or no ').upper()
    if play_again == 'YES':
        question_allocation()

print '\nWelcome to the quiz!\n'
question_allocation()
raw_input('Press Enter to exit')

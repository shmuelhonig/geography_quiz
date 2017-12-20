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


def again():
    """
    Behavior: Asks user if user wants to play again. Prompts user again if
    invalid selection is made.
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
        level()


def you_are_incorrect(key, value, num_attempts, correct_answers):
    """
    Behavior: For wrong answers, tells user how many attempts are left, and, if
    appropriate, prompts the user to give another answer.
    : Parameters: The current blank number, the correct answer for the given
    blank, the number of attempts the user has chosen to get, and the number of
    blanks that have been answered correctly.
    : Return: None (prints some messages).
    """
    attempts_taken = 1
    while attempts_taken < num_attempts:
        print '\nThat is incorrect. You have ' + str(
            num_attempts - attempts_taken) + ' attempts remaining\n'
        user_answer = raw_input(
            'What should be substituted for ' + key + '? ').upper()
        if user_answer == value:
            print '\nCorrect!'
            correct_answers[0] += 1
            break
        attempts_taken = attempts_taken + 1
    if attempts_taken == num_attempts:
        print '\nThat is incorrect. You have no more attempts'


def play_quiz(which_question, which_dictionary, num_attempts):
    """
    Behavior: Initiates the quiz. Prompts user to fill in the blanks, one at a
    time. Upon completion of game, lets user know how many questions they
    answered correctly.
    : Parameters: The question chosen by the user, the dictionary containing
    the appropriate answers, and the number of attempts the user has chosen to
    get.
    : Return: None (directs the program to other functions and prints some
    messages).
    """
    blanks_completed = 0
    correct_answers = [0]
    updated_question = ''
    for key, value in sorted(which_dictionary.iteritems()):
        user_answer = raw_input(
            '\nWhat should be substituted for ' + key + '? ').upper()
        if user_answer == value:
            print '\nCorrect!'
            correct_answers[0] += 1
        else:
            you_are_incorrect(key, value, num_attempts, correct_answers)
        if blanks_completed == 0:
            # When the first blank in the question is filled, the original
            # question must be updated. When subsequent blanks are filled, the
            # updated question must be updated.
            updated_question = which_question.replace(key, value)
        else:
            updated_question = updated_question.replace(key, value)
        print "\n" + updated_question
        blanks_completed = blanks_completed + 1
    print '\nThanks for playing! You answered ' + str(correct_answers[0]) +\
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


def question_allocation(selected_level):
    """
    Behavior: Allocates the appropriate question and dictionary to be used in
    the quiz based on user input.
    : Parameters: The level selected by the user.
    : Return: None (Prints the appropriate question and directs program to
    another function).
    """
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
    play_quiz(question, answers_dictionary, num_attempts)


def level():
    """
    Behavior: Collects user input for which level of quiz to play. Prompts user
    again if invalid selection is made.
    : Parameters: None.
    : Return: None (prints messages and directs program to another function).
    """
    print '\nThere are three levels: easy, medium, and hard.'
    level_options = ['EASY', 'MEDIUM', 'HARD']
    chosen_level = raw_input('Type your preference and press enter ').upper()
    while chosen_level not in level_options:
        print '\nInvalid selection.\n'
        chosen_level = raw_input(
            'Type your preference and press enter ').upper()
    question_allocation(chosen_level)

print '\nWelcome to the quiz!'
level()
raw_input('Press Enter to exit')

import os
import math_functions as mf

number_of_problems = 10


def intro_screen() -> int:
    """provides introduction text to user and returns the game the user would like to play"""
    print(
        f"Welcome to Mini Math! Please select from the options below. You will be given {number_of_problems} math problems and a score at the end.")

    game_selected = None

    while game_selected not in game_dict.keys():
        print("Please select from the following options:")

        for k, v in game_dict.items():
            print(k, v[1])

        game_selected = user_input()

        while game_selected > len(game_dict.keys()):

            print("Please select a valid option")
            game_selected = user_input()

    os.system('cls')
    return game_selected


def game_loop(game_selected, correct_answers):

    answer = game_dict[game_selected][0]()
    user_answer = user_input()

    if user_answer == answer:
        print('correct!\r\n')
        correct_answers += 1

    else:
        print('incorrect!\r\n')

    return correct_answers


def user_input() -> int:
    """asks the user for input and makes sure the output is always a positive integer"""
    choice = input().lower()

    while not choice.isdigit():
        print("Positive integers only, please!")
        choice = input().lower()

    choice = int(choice)

    return choice


def results(number_of_problems, correct_answers):
    """provides statistics to the user"""
    percent_correct = float(correct_answers)/number_of_problems

    print(f"You got {correct_answers} out of {number_of_problems} problems correct.\r\nThat's an accuracy rating of {percent_correct*100}%!")
    print("Would you like to play again?: yes/no")

    return input()


game_dict = {1: [mf.addition_problem, 'addition'],
             2: [mf.subtraction_problem, 'subtraction'],
             3: [mf.multiplication_problem, 'multiplication'],
             4: [mf.division_problem, 'division']}


def main():
    correct_answers = 0
    game_selected = intro_screen()

    for i in range(number_of_problems):
        correct_answers = game_loop(game_selected, correct_answers)

    play_again = results(number_of_problems, correct_answers)
    if play_again == 'yes':
        print('\r\n')
        main()
    else:
        print('Goodbye!')
        input()


if __name__ == "__main__":
    main()

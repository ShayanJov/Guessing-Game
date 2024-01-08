import json
import random
import os
from .animation_helper import animate_text
from Classes.league_table_manager import LeagueTableManager

@staticmethod
def load_all_questions():
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.realpath(__file__))
        
    # Construct the path to the JSON file inside the 'jsons' folder
    json_file_path = os.path.join(script_directory, '../jsons/questions_and_answers.json')

    # Load all questions from the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        questions_data = json.load(json_file)
            
    # Shuffle the questions_data list to randomize the order of questions
    random.shuffle(questions_data)

    return questions_data

@staticmethod
def play_game(player_name, num_questions, max_attempts, max_fails, game_mode):  # Fix the function name
    # Initialize score and question attempts
    score = 0
    questions_failed = 0

    # Load all questions
    questions_data = load_all_questions()

    if num_questions is None:
        selected_questions = questions_data
    else:
        # Select a fixed number of questions
        selected_questions = random.sample(questions_data, num_questions)

    for question_data in selected_questions:
        question = question_data['question']
        answer = question_data['answer']
        emoji = question_data['emoji']

        # Reset attempts for each question
        attempts_left = max_attempts

        while attempts_left > 0:
            user_answer = input(f"\n\033[1;36mQuestion:\033[0m {question}\n\033[1;35mYour Answer:\033[0m ").strip().lower()
            if user_answer == '0':
                return 0
            if user_answer == answer.lower():
                animate_text("\033[1;32mCorrect! You earned a point.\033[0m\n")
                score += 1
                break
            else:
                attempts_left -= 1
                animate_text(f"\033[1;91mIncorrect! {attempts_left} {'attempts' if attempts_left > 1 else 'attempt'} remaining.\033[0m\n")
                if attempts_left == 0 and questions_failed != max_fails:
                    questions_failed += 1
                    if questions_failed != max_fails:
                        animate_text(f"\033[1;91mGame over for this question. The correct answer was:\033[0m{emoji} {answer}\n")
                    break

        if questions_failed == max_fails:
            animate_text(f"\033[1;91mGame over. The correct answer was:\033[0m{emoji} {answer}\n")
            break  # End the loop for the current question

    animate_text(f"\n\033[1;34mGame over for {player_name}.\033[0m Your final score is \033[1;93m{score}\033[0m.\n")
        
    league_table_instance = LeagueTableManager()
    # Update the player's score in the league table
    league_table_instance.update_player_score(player_name, score, game_mode)

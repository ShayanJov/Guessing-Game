import json
import random
import os
from Classes.league_table_manager import LeagueTableMethods 

class GameLogic:

    def select_random_questions(self, num_questions):
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))
        
        # Construct the path to the JSON file inside the 'jsons' folder
        json_file_path = os.path.join(script_directory, '../jsons/questions_and_answers.json')

        # Load questions from the JSON file
        with open(json_file_path, 'r') as json_file:
            questions_data = json.load(json_file)

        # Select a random subset of questions
        selected_questions = random.sample(questions_data, num_questions)

        return selected_questions

    def play_game(self, player_name):
        # Initialize score and question attempts
        score = 0
        max_attempts = 3

        # Select 6 random questions
        selected_questions = self.select_random_questions(6)

        for question_data in selected_questions:
            question = question_data['question']
            answer = question_data['answer']

            # Reset attempts for each question
            attempts_left = max_attempts

            while attempts_left > 0:
                user_answer = input(f"\nQuestion: {question}\nYour Answer: ").strip().lower()
                if user_answer == "back":
                    break
                if user_answer == answer.lower():
                    print("Correct! You earned a point.")
                    score += 1
                    break
                else:
                    attempts_left -= 1
                    print(f"Incorrect! {attempts_left} {'attempts' if attempts_left > 1 else 'attempt'} remaining.")

            if attempts_left == 0:
                print("Game over for this question. The correct answer was:", answer)

        print(f"\nGame over for {player_name}. Your final score is {score}.")
        
        league_table_instance = LeagueTableMethods()
        # Update the player's score in the league table
        league_table_instance.update_player_score(player_name, score)

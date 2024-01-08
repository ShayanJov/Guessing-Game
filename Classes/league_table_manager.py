import json
import os
from .animation_helper import animate_text

class LeagueTableManager:
    @staticmethod
    def load_league_data(json_file_name):
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))
        
        # Construct the path to the JSON file inside the 'jsons' folder
        json_file_path = os.path.join(script_directory, f'../jsons/{json_file_name}')

        try:
            with open(json_file_path, 'r') as json_file:
                loaded_data = json.load(json_file)
                return loaded_data
        except FileNotFoundError:
            return []

    @staticmethod
    def display_league_table_and_prompt(user_name, game_mode, num_players_to_show):
        json_file_name = f'league_table_{game_mode.lower()}.json'
        league_data = LeagueTableManager.load_league_data(json_file_name)

        if not league_data:
            print(f"\033[1;31mNo data available in the {game_mode.upper()} league table.\033[0m")
            return

        print(f"\n\033[1;34m{game_mode.upper()} LEAGUE TABLE\033[0m:")

        # Sort players based on best score
        sorted_players = LeagueTableManager.sort_players_by_score(league_data)

        while True:
            for rank, player in enumerate(sorted_players[:num_players_to_show], start=1):
                player_info = {key: value for key, value in player.items() if key != "password"}
                if player_info['player_name'] == user_name:
                    print(f"\033[1;32m{player_info['player_name']}\033[0m - Your Score: \033[1;33m{player_info['player_best_score']}\033[0m\n")
                else:
                    print(f"\033[1;36m{rank}. {player_info['player_name']}\033[0m - Score: \033[1;33m{player_info['player_best_score']}\033[0m\n")

            try:
                num_to_show_more = int(input("\033[1mEnter the number of additional players to show (enter 0 to go back): \033[0m"))
            except ValueError:
                animate_text("\033[1;31m❌ Invalid input. Please enter a number. ❌\033[0m")
                continue

            if num_to_show_more == 0:
                break
            elif num_to_show_more < 0:
                animate_text("\033[1;31m❌ Please enter a non-negative number. ❌\033[0m")
            else:
                num_players_to_show += num_to_show_more



    @staticmethod
    def save_league_data(league_data, json_file_name):
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))

        # Construct the path to the JSON file inside the 'jsons' folder
        json_file_path = os.path.join(script_directory, f'../jsons/{json_file_name}')

        with open(json_file_path, 'w') as json_file:
            json.dump(league_data, json_file, indent=2)

    @staticmethod
    def update_player_score(player_name, new_score, game_mode):
        json_file_name = f'league_table_{game_mode.lower()}.json'
        league_data = LeagueTableManager.load_league_data(json_file_name)

        # Find the player in the league_data
        for player in league_data:
            if player["player_name"] == player_name:
                # Check if the new score is higher
                if new_score > int(player["player_best_score"]):
                    player["player_best_score"] = new_score
                    print(f"\033[1;32mScore updated successfully for {player_name}. New score: {new_score}\033[0m")
                else:
                    print(f"\033[1;31mThe new score ({new_score}) is not higher than the existing score ({player['player_best_score']}).\033[0m")
                break
        else:
            # If the player is not in the league_data, add a new entry with the game_mode field
            league_data.append({"player_name": player_name.lower(), "player_best_score": new_score})
            print(f"\033[1;32mNew record for {player_name} added with a score of {new_score} in game mode {game_mode}\033[0m")

        # Save the updated league data
        LeagueTableManager.save_league_data(league_data, json_file_name)



    @staticmethod
    def sort_players_by_score(league_data):
        # Sort the players by best score in descending order
        sorted_players = sorted(league_data, key=lambda x: int(x["player_best_score"]), reverse=True)

        return sorted_players

import json
import os

class LeagueTableManager:
    @staticmethod
    def load_league_data():
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))
        
        # Construct the path to the JSON file inside the 'jsons' folder
        json_file_path = os.path.join(script_directory, '../jsons/league_table.json')

        try:
            with open(json_file_path, 'r') as json_file:
                loaded_data = json.load(json_file)
                return loaded_data
        except FileNotFoundError:
            return []

    @staticmethod
    def display_league_table():
        print("\n\033[1;34mLEAGUE TABLE\033[0m:")  # Bold and Blue color for LEAGUE TABLE
        for player in LeagueTableManager.load_league_data():
            player_info = {key: value for key, value in player.items() if key != "password"}
            print(f"\033[1;36m{player_info['player_name']}\033[0m - Score: \033[1;33m{player_info['player_best_score']}\033[0m")

    @staticmethod
    def save_league_data(league_data):
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))

        # Construct the path to the JSON file inside the 'jsons' folder
        json_file_path = os.path.join(script_directory, '../jsons/league_table.json')

        # Call group_and_rank_players to get the grouped and sorted data
        grouped_and_sorted_data = LeagueTableManager.group_and_rank_players(league_data)

        with open(json_file_path, 'w') as json_file:
            json.dump(grouped_and_sorted_data, json_file, indent=2)

    @staticmethod
    def update_player_score(player_name, new_score, game_mode):
        league_data = LeagueTableManager.load_league_data()

        # Find the player in the league_data
        for player in league_data:
            if player["player_name"] == player_name and player.get("game_mode") == game_mode:
                # Check if the new score is higher
                if new_score > int(player["player_best_score"]):
                    player["player_best_score"] = str(new_score)
                    print(f"\033[1;32mScore updated successfully for {player_name}. New score: {new_score}\033[0m")
                else:
                    print(f"\033[1;31mThe new score ({new_score}) is not higher than the existing score ({player['player_best_score']}).\033[0m")
                break
        else:
            # If the player is not in the league_data, add a new entry with the game_mode field
            league_data.append({"player_name": player_name.lower(), "player_best_score": new_score, "game_mode": game_mode})
            print(f"\033[1;32mNew record for {player_name} added with a score of {new_score} in game mode {game_mode}\033[0m")

        # Save the updated league data  
        LeagueTableManager.save_league_data(league_data)


    @staticmethod
    def group_and_rank_players(league_data):
        # Group players by game mode
        grouped_players = {}

        for player in league_data:
            game_mode = player.get("game_mode")
            player_name = player["player_name"]
            score = player["player_best_score"]

            if game_mode not in grouped_players:
                grouped_players[game_mode] = []

            # If player_name is not in the list or has a higher score, update the best score
            existing_player = next((p for p in grouped_players[game_mode] if p["player_name"] == player_name), None)
            if existing_player:
                existing_player["player_best_score"] = max(existing_player["player_best_score"], score)
            else:
                grouped_players[game_mode].append({
                    "player_name": player_name,
                    "player_best_score": score,
                    "game_mode": game_mode
                })

        # Sort the players within each group by best score
        for game_mode, players in grouped_players.items():
            grouped_players[game_mode] = sorted(players, key=lambda x: x["player_best_score"], reverse=True)

        # Flatten the grouped data into a list of dictionaries
        result_list = [player for players in grouped_players.values() for player in players]

        return result_list
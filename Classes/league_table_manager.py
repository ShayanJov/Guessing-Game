import json
import os

class LeagueTableMethods:
    @staticmethod
    def load_league_data():
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))
        
        # Construct the path to the JSON file inside the 'jsons' folder
        json_file_path = os.path.join(script_directory, '../jsons/league_table.json')

        try:
            with open(json_file_path, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return []

    @staticmethod
    def display_league_table():
        print("\nLEAGUE TABLE:")
        for player in LeagueTableMethods.load_league_data():
            print(f"{player['player_name']} - Score: {player['player_score']}")
        print()

    @staticmethod
    def save_league_data(league_data):
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))
        
        # Construct the path to the JSON file inside the 'jsons' folder
        json_file_path = os.path.join(script_directory, '../jsons/league_table.json')

        # Sort the league_data based on player_score
        league_data.sort(key=lambda x: int(x["player_score"]), reverse=True)
        
        with open(json_file_path, 'w') as json_file:
            json.dump(league_data, json_file, indent=2)

    @staticmethod
    def update_player_score(player_name, new_score):
        league_data = LeagueTableMethods.load_league_data()
        # Find the player in the league_data
        for player in league_data:
            print(f"Checking player in loop: {player['player_name']}")
            if player["player_name"] == player_name:
                # Check if the new score is higher
                if new_score > int(player["player_score"]):
                    player["player_score"] = str(new_score)
                    print(f"Score updated successfully for {player_name}. New score: {new_score}")
                else:
                    print(f"The new score ({new_score}) is not higher than the existing score ({player['player_score']}).")
                break
        else:
            # If the player is not in the league_data, add a new entry
            league_data.append({"player_name": player_name.lower(), "player_score": new_score})
            # Save the updated league data
            LeagueTableMethods.save_league_data(league_data)
            print(f"New player {player_name} added with a score of {new_score}")

    @staticmethod
    def check_existing_players(player_name):
        league_table = LeagueTableMethods.load_league_data()
        for player in league_table:
            if player_name.lower() == player['player_name'].lower():
                return True
        return False
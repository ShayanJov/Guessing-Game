import json
from .league_table_manager import LeagueTableMethods

def existing_player_menu():
    while True:
        league_table = LeagueTableMethods()
        player_name = input("Enter your player name (type 'back' to return to the main menu): ")

        if player_name.lower() == 'back':
            print("Returning to the main menu.")
            return None  # Indicate that the user chose to go back
        
        if league_table.check_existing_players(player_name):
            return player_name
        else:
            print(f"The player {player_name} does not exist. Please try again.")
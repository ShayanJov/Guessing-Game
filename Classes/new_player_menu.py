from .league_table_manager import LeagueTableMethods

def add_new_player(player_name):
    league_table_instance = LeagueTableMethods()
    league_table_instance.update_player_score(player_name, 0)
    

def new_player_menu():
    while True:
        league_table_instance = LeagueTableMethods()
        user_input_name = input("Enter your player name (type 'back' to return to the main menu): ")

        if user_input_name.lower() == 'back':
            print("Returning to the main menu.")
            return None  # Indicate that the user chose to go back

        # Check if the player name already exists
        if league_table_instance.check_existing_players(user_input_name):
            print("Sorry, that player name is already taken. Please choose another name.")
        else:
            print(f"Welcome, {user_input_name}! You are now a new player.")
            return user_input_name

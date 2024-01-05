from .league_table_manager import LeagueTableMethods
from .new_player_menu import new_player_menu
from .game_logic import GameLogic
from .existing_player_menu import existing_player_menu

def display_main_menu():
    league_table_instance = LeagueTableMethods()
    game_logic_instance = GameLogic()

    while True:
        print("\nMAIN MENU:")
        print("1. League Table")
        print("2. New Player")
        print("3. Existing Player")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            league_table_instance.display_league_table()
        elif choice == '2':
            player_name = new_player_menu()
            if player_name is None:  # If the user chose to go back
                continue
            else:
                game_logic_instance.play_game(player_name)
        elif choice == '3':
            player_name = existing_player_menu()
            if player_name is None:  # If the user chose to go back
                continue
            game_logic_instance.play_game(player_name)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            return False
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
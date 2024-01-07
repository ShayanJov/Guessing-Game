from .league_table_manager import LeagueTableManager
from .game_menu import display_game_menu

def display_main_menu(player_name):
    league_table_instance = LeagueTableManager()
    first_time = True

    while True:
        if first_time:
            print(f"\nHello \033[1;32m{player_name}\033[0m")  # Green color for player_name
        elif not first_time:
            print(f"\n\033[1;36m{player_name}\033[0m")  # Cyan color for player_name

        print("\033[1mMAIN MENU:\033[0m")  # Bold formatting for MAIN MENU
        print("1. \033[1;33mplay a new game\033[0m")  # Yellow color for Play the Game
        print("2. \033[1;34msee the League Table\033[0m")  # Blue color for See the League Table
        print("3. \033[1;35mchange User\033[0m")  # Magenta color for Change User
        print("0. \033[1;31mexit\033[0m")  # Red color for Exit

        choice = input("\033[1mEnter your choice:\033[0m ")

        if first_time:
            first_time = False

        if choice.lower() in ["1", "play"]:
            display_game_menu(player_name)
        elif choice.lower() in ["2", "see"]:
            # Call the function to display the league table
            league_table_instance.display_league_table()
        elif choice.lower() in ["3", "change"]:
            return "goback"  # indicates that the user wants to go back to the login and register menu
        elif choice.lower() in ["0", "exit"]:
            return "exit"  # indicates that the user wants to exit
        else:
            print("\033[1;31mInvalid choice. Please enter a number from 0 to 3.\033[0m")

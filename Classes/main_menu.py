from .animation_helper import animate_text
from .game_menu import display_game_menu
from .league_table_menu import display_league_menu

def display_main_menu(user_name):
    first_time = True

    while True:
        if first_time:
            print(f"\n\033[1;32m👋 Hello {user_name}! 👋\033[0m")  # Green color for user_name
        elif not first_time:
            print(f"\n\033[1;36m{user_name}\033[0m")  # Cyan color for user_name

        print("\033[1mMAIN MENU:\033[0m")  # Bold formatting for MAIN MENU
        print("1. \033[1;33m🎮 Play a new game\033[0m")  # Yellow color for Play the Game
        print("2. \033[1;34m📊 See the League Table\033[0m")  # Blue color for See the League Table
        print("3. \033[1;35m🚪 Logout\033[0m")  # Magenta color for Logout
        print("0. \033[1;31m👋 Exit\033[0m")  # Red color for Exit

        choice = input("\033[1mEnter your choice: \033[0m")

        if first_time:
            first_time = False

        if choice.lower() in ["1", "play"]:
            display_game_menu(user_name)
        elif choice.lower() in ["2", "see"]:
            display_league_menu(user_name)
        elif choice.lower() in ["3", "logout"]:
            animate_text("\033[1;35mLogging out... Goodbye! 👋\033[0m\n")
            return "goback"  # Indicates that the user wants to go back to the login and register menu
        elif choice.lower() in ["0", "exit"]:
            animate_text(f"\n\033[1;31m👋 Goodbye {user_name}! Thanks for playing! 👋\033[0m\n")
            return "exit"  # Indicates that the user wants to exit
        else:
            animate_text("\033[1;31m❌ Invalid choice. Please enter a number from 0 to 3. ❌\033[0m\n")

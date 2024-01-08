from .animation_helper import animate_text
from .game_mode_helper import GameLogic

# Function to call the game from another file
def display_game_menu(player_name):
    while True:
        # Choose game mode: 1 for 'classic', 2 for 'easy', 3 for 'normal', 4 for 'hard', 5 for 'more info'
        print("\n\033[1;36m🎮 Choose game mode: 🎮\033[0m")
        print("  \033[1;36m1. 🏰 Classic\033[0m")
        print("  \033[1;33m2. 🌳 Easy\033[0m")
        print("  \033[1;91m3. 🌍 Normal\033[0m")
        print("  \033[1;93m4. 🔥 Hard\033[0m")
        print("  \033[1;35m5. ℹ️ More Information\033[0m")
        print("  \033[1;31m0. 🚪 Go back\033[0m")

        game_mode = input("\033[1mEnter your choice: \033[0m")

        if game_mode.lower() in ["0", "back"]:
            animate_text("\033[1mReturning to the main menu.\033[0m\n")
            break

        if game_mode.lower() in ["1", "classic"]:
            GameLogic.play_classic_mode(player_name)
        elif game_mode.lower() in ["2", "easy"]:
            GameLogic.play_easy_mode(player_name)
        elif game_mode.lower() in ["3", "normal"]:
            GameLogic.play_normal_mode(player_name)
        elif game_mode.lower() in ["4", "hard"]:
            GameLogic.play_hard_mode(player_name)
        elif game_mode.lower() in ["5", "more info"]:
            display_game_modes_info()
        else:
            animate_text("\033[1;91mInvalid selection. Please try again.\033[0m\n")

def display_game_modes_info():
    print("\n\033[1;35mℹ️ Game Modes Information:\033[0m")
    print("  \033[1;36m1. 🏰 Classic: \033[0mAnswer 6 questions with three chances each. Accumulate points for correct answers.")
    print("  \033[1;33m2. 🌳 Easy: \033[0mAnswer questions with three chances each. Fail three times and the game ends.")
    print("  \033[1;91m3. 🌍 Normal: \033[0mAnswer questions with three chances each. One wrong answer ends the game.")
    print("  \033[1;93m4. 🔥 Hard: \033[0mAnswer questions, but one wrong answer ends the game instantly. No second chances.")

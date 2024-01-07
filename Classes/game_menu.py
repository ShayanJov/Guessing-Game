from Classes.game_logic import GameLogic

# Function to call the game from another file
def display_game_menu(player_name):
    game_logic = GameLogic()

    while True:
        # Choose game mode: 1 for 'easy', 2 for 'normal', 3 for 'hard', 4 for 'classic'
        print("\n\033[1mChoose game mode:\033[0m")
        print("  \033[1;36m1. Easy\033[0m")
        print("  \033[1;33m2. Normal\033[0m")
        print("  \033[1;91m3. Hard\033[0m")
        print("  \033[1;93m4. Classic\033[0m")
        print("  \033[1;31m0. Go back\033[0m")

        game_mode = input("\033[1mEnter your choice:\033[0m ")

        if game_mode.lower() in ["0", "back"]:
            print("\033[1mReturning to the main menu.\033[0m")
            break

        if game_mode.lower() in ["1", "easy"]:
            game_logic.play_easy_mode(player_name)
        elif game_mode.lower() in ["2", "normal"]:
            game_logic.play_normal_mode(player_name)
        elif game_mode.lower() in ["3", "hard"]:
            game_logic.play_hard_mode(player_name)
        elif game_mode.lower() in ["4", "classic"]:
            game_logic.play_classic_mode(player_name)
        else:
            print("\033[1;91mInvalid selection. Please try again.\033[0m")
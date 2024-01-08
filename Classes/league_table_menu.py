import time
import sys
from .league_table_manager import LeagueTableManager

def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def display_league_menu(user_name):
    while True:
        print("\n\033[1;34m🏆 LEAGUE TABLE MENU 🏆\033[0m:")
        print("1. \033[1;33m🏰 Classic\033[0m")
        print("2. \033[1;32m🌳 Easy\033[0m")
        print("3. \033[1;36m🌍 Normal\033[0m")
        print("4. \033[1;31m🔥 Hard\033[0m")
        print("0. \033[1;35m🚪 Go back\033[0m")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            LeagueTableManager.display_league_table_and_prompt(user_name, "classic", 10) #10 is default number of players to show
        elif choice == "2":
            LeagueTableManager.display_league_table_and_prompt(user_name, "easy", 10)
        elif choice == "3":
            LeagueTableManager.display_league_table_and_prompt(user_name, "normal", 10)
        elif choice == "4":
            LeagueTableManager.display_league_table_and_prompt(user_name, "hard", 10)
        elif choice == "0":
            animate_text("\033[1mReturning to the main menu.\033[0m\n")
            break
        else:
            animate_text("\033[1;31mInvalid choice. Please enter a number from 1 to 5.\033[0m")

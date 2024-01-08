import time
from .animation_helper import animate_text
from .user_password_manager import UserPaswordManager
from .main_menu import display_main_menu

def login_menu():
    while True:
        print("\n\033[1;34m🔐 Login Menu 🔐\033[0m")  # Bold and Blue color for Login Menu
        
        player_name = input("\033[1mEnter your player name (\033[1;31mtype '0' to return to the main menu\033[0m): \033[0m")

        if player_name.lower() == '0':
            print("\033[1mReturning to the main login.\033[0m\n")
            return "goback"  # Indicate that the user chose to go back

        entered_password = input("\033[1mEnter your password (\033[1;31mtype '0' to return to the main menu\033[0m): \033[0m")

        if entered_password == '0':
            print("\033[1mReturning to the main login.\033[0m\n")
            return '0'  # Indicate that the user chose to go back

        print("\n\033[1;36m🔄 Authenticating... 🔄\033[0m")
        time.sleep(2)  # Simulate authentication delay

        if UserPaswordManager.check_password(player_name, entered_password):
            animate_text("\033[1;32m✔ Authentication successful! ✔\033[0m\n")  # Green color for success
            time.sleep(1)  # Short delay for success message
            result = display_main_menu(player_name)
            
            if result == "goback": # User wants to go back to login and register menu
                return "goback"
            elif result == "exit": # Indicates that user wants to exit
                return "exit"

        else:
            animate_text("\033[1;31m❌ Incorrect username or password. Please try again. ❌\033[0m\n")  # Red color for error
            time.sleep(1)  # Short delay for error message

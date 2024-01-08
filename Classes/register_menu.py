import time
from .animation_helper import animate_text
from .user_password_manager import UserPaswordManager
from .main_menu import display_main_menu

def register_menu():
    while True:
        print("\n\033[1;34m📝 Register Menu 📝\033[0m")  # Bold and Blue color for Register Menu
        user_name = input("\033[1mEnter a unique player name (\033[1;31mtype '0' to return to the login menu\033[0m): \033[0m")

        if user_name.lower() == '0':
            print("\033[1mReturning to the main register menu.\033[0m")
            return 0  # Indicate that the user chose to go back

        if UserPaswordManager.check_existing_users(user_name):
            print(f"\033[1;31mThe player {user_name} already exists. Please choose another name.\033[0m")
        else:
            entered_password = input("\033[1mEnter a password (\033[1;31mtype '0' to return to the main menu\033[0m): \033[0m")
            if entered_password.lower() == '0':
                print("\033[1mReturning to the main register menu.\033[0m")
                return 0  # Indicate that the user chose to go back
            
            print("\033[1;36m🔄 Registering... 🔄\033[0m")
            time.sleep(2)  # Simulate registration delay
            
            UserPaswordManager.add_user(user_name, entered_password)
            
            animate_text(f"\033[1;32m✔ Player {user_name} registered successfully! ✔\033[0m\n")  # Green color for success
            time.sleep(1)  # Short delay for success message
            
            result = display_main_menu(user_name)
            if result == "goback": # User wants to go back to login and register menu
                return "goback"
            elif result == "exit": # Indicates that user wants to exit
                return "exit"

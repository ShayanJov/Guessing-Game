from .user_password_manager import UserPaswordManager
from .main_menu import display_main_menu

def register_menu():
    while True:
        league_table = UserPaswordManager()
        print("\n\033[1;34mRegister Menu\033[0m")  # Bold and Blue color for Register Menu
        user_name = input("\033[1mEnter a unique player name (\033[1;31mtype '0' to return to the login menu\033[0m): \033[0m")

        if user_name.lower() == '0':
            print("\033[1mReturning to the main register menu.\033[0m")
            return 0  # Indicate that the user chose to go back

        if league_table.check_existing_users(user_name):
            print(f"\033[1;31mThe player {user_name} already exists. Please choose another name.\033[0m")
        else:
            entered_password = input("\033[1mEnter a password (\033[1;31mtype '0' to return to the main menu\033[0m): \033[0m")
            if entered_password.lower() == '0':
                print("\033[1mReturning to the main register menu.\033[0m")
                return 0  # Indicate that the user chose to go back
            
            league_table.add_user(user_name, entered_password)
            
            print(f"\033[1;32mPlayer {user_name} registered successfully.\033[0m")
            result = display_main_menu(user_name)
            if result == "goback": #user wants to go back to login and register menu
                return "goback"
            elif result == "exit": #indicates that user wants to exit
                return "exit"

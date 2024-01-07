from .user_password_manager import UserPaswordManager
from .main_menu import display_main_menu

def login_menu():
    while True:
        user_password_manager = UserPaswordManager()
        print("\n\033[1;34mLogin Menu\033[0m")  # Bold and Blue color for Login Menu
        player_name = input("\033[1mEnter your player name (\033[1;31mtype '0' to return to the main menu\033[0m): \033[0m")

        if player_name.lower() == '0':
            print("\033[1mReturning to the main login.\033[0m")
            return "goback"  # Indicate that the user chose to go back

        entered_password = input("\033[1mEnter your password (\033[1;31mtype '0' to return to the main menu\033[0m): \033[0m")

        if entered_password == '0':
            print("\033[1mReturning to the main login.\033[0m")
            return '0'  # Indicate that the user chose to go back

        if user_password_manager.check_password(player_name, entered_password):
            result = display_main_menu(player_name)
            if result == "goback": #user wants to go back to login and register menu
                return "goback"
            elif result == "exit": #indicates that user wants to exit
                return "exit"

        else:
            print("\033[1;31mIncorrect username or password. Please try again.\033[0m")
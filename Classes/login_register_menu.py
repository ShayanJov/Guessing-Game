import time
import sys
from .animation_helper import animate_text
from .login_menu import login_menu
from .register_menu import register_menu

def login_register_menu(first_time=True):
    loading_message = "\033[1;36m🔄 Loading... 🔄\033[0m"
    
    while True:
        if first_time:
            print("\n\033[1;36m🎮 Welcome to the Game! 🎮\033[0m")
            animate_text(loading_message)
            time.sleep(2)  # Display the loading animation for 2 seconds
            sys.stdout.write("\r\033[K")  # Clear the loading message
            sys.stdout.flush()
            first_time = False  # Set the flag to False after displaying welcome and loading

        print("\033[1m1. \033[1;33m🔒 Login\033[0m")
        print("\033[1m2. \033[1;34m📝 Register\033[0m")
        print("\033[1;31m0. 🚪 Exit\033[0m")
        user_input = input("\033[1mEnter your choice: \033[0m")

        result = ''
        if user_input.lower() in ["1", "login"]:
            result = login_menu()
        elif user_input.lower() in ["2", "register"]:
            result = register_menu()
        elif user_input.lower() in ["0", "exit"]:
            print("\n\033[1;31m👋 Exiting the program. Goodbye! 👋\033[0m")
            return "exit"
        else:
            print("\033[1;31m❌ Invalid choice. Please select a valid option. ❌\033[0m\n")

        if result == "goback":
            first_time = False
        elif result == "exit":
            return "exit"

from .login_menu import login_menu
from .register_menu import register_menu

def login_register_menu(first_time=True):
    while True:
        if first_time:
            print("\n\033[1;36mWelcome to the Game!\033[0m")  # Cyan color for Welcome to the Game!
        else:
            print("\n")

        print("\033[1m1. \033[1;33mLogin\033[0m")  # Bold and Yellow color for Login
        print("\033[1m2. \033[1;34mRegister\033[0m")  # Bold and Blue color for Register
        print("\033[1;31m0. Exit\033[0m")  # Red color for Exit
        user_input = input("\033[1mEnter your choice:\033[0m ")

        result = ''
        if user_input.lower() in ["1", "login"]:
            result = login_menu()
        elif user_input.lower() in ["2", "register"]:
            result = register_menu()
        elif user_input.lower() in ["0", "exit"]:
            print("\n\033[1;31mExiting the program. Goodbye!\033[0m")
            return "exit"  # exiting program
        else:
            print("\033[1;31mInvalid choice. Please select a valid option.\033[0m")

        if result == "goback":  # Coming back from the register_login_menu
            # Update the flag after the first iteration
            first_time = False
        elif result == "exit":
            return "exit"  # exiting program

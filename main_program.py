import os
import subprocess
from Classes.login_register_menu import login_register_menu

def install_dependencies():
    try:
        print("First time on a new computer - installing dependencies.")
        # Redirect stdout and stderr to subprocess.PIPE to suppress the output
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Dependencies installed successfully.")
        
        # Create a marker file to indicate that dependencies are installed
        with open(".installed", "w") as marker_file:
            pass
    except subprocess.CalledProcesasError as e:
        print(f"Error installing dependencies: {e}")
        exit(1)

def check_dependencies_installed():
    return os.path.exists(".installed")

if __name__ == "__main__":
    if not check_dependencies_installed():
        # Dependencies not installed, so install them
        install_dependencies()

    while True:
        try:
            if login_register_menu() == "exit":
                break
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"An error occurred: {e}")

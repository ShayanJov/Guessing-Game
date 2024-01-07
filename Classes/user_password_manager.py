import json
import os
import bcrypt

class UserPaswordManager:
    @staticmethod
    def load_user_data_table():
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))
        
        # Construct the path to the JSON file inside the 'jsons' folder
        json_file_path = os.path.join(script_directory, '../jsons/user_password.json')

        try:
            with open(json_file_path, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return []
        
    @staticmethod
    def save_user_data(user_data):
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))

        # Construct the path to the JSON file inside the 'jsons' folder
        json_file_path = os.path.join(script_directory, '../jsons/user_password.json')

        with open(json_file_path, 'w') as json_file:
            json.dump(user_data, json_file, indent=2)

    @staticmethod
    def check_existing_users(user_name):
        user_data = UserPaswordManager.load_user_data_table()
        for user in user_data:
            if user_name.lower() == user['user_name'].lower():
                return True
        return False
    
    @staticmethod
    def check_password(player_name, entered_password):
        league_table = UserPaswordManager.load_user_data_table()

        for player in league_table:
            if (
                player_name.lower() == player['user_name'].lower()
                and bcrypt.checkpw(entered_password.encode('utf-8'), player['password'].encode('utf-8'))
            ):
                return True

        return False
    
    @staticmethod
    def add_user(player_name, entered_password):
        user_table_data = UserPaswordManager.load_user_data_table()

        # Hash the password before saving it
        hashed_password = bcrypt.hashpw(entered_password.encode('utf-8'), bcrypt.gensalt())

        # Convert the byte-like object to a string for JSON serialization
        hashed_password_str = hashed_password.decode('utf-8')

        new_user = {
            'user_name': player_name,
            'password': hashed_password_str,
        }

        user_table_data.append(new_user)
        UserPaswordManager.save_user_data(user_table_data)
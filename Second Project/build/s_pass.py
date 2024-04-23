import random
import json
import os

# Create our customize class - "Suggest_pass"
class Sug_and_Save_data:
    # Method for creating a password
    def create_password(self):
        # Set all characters that can be in the password
        upper_letters = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"
        lower_letters = upper_letters.lower()
        numbers = "0123456789"
        symbols = "!@#$^&*_№%+=-.,"
        
        all_chars = upper_letters + lower_letters + numbers + symbols
        # Randomize the length of password
        pass_length = random.randint(14, 17)
        # Create and return it
        password = "".join(random.sample(all_chars, pass_length))
        return password
    
    # Method for saving data in the json file
    def save_data_to_json(self, json_file_path, username, password):
        
        # Read json file
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        
        # Get new data and save it in the variable
        new_data = {
            "username" : username,
            "password" : password
        }
        # Set our new data (in last position) in our list with already loaded data
        len_num_list = len(data)
        data.insert(len_num_list,new_data)
        
        # Write json file with all data
        with open(json_file_path, "w") as jf:
            json.dump(data, jf, indent=5)
import random

# Create our customize class - "Suggest_pass"
class Suggest_pass:
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
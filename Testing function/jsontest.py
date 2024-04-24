import json
# ==========================================================================================
        
new_file = r"C:\Users\Christian\Desktop\Python projects\Testing function\new_file.json"
with open(new_file, "r") as jf:
    loaded_data = json.load(jf)

old_data_list = loaded_data["data"]

new_data = {
    "username": "user_test1",
    "password": "pass_test1"
}

new_new_data = {
    "username": "user_test2",
    "password": "pass_test2"
}

new_old_data = {
    "username": "user_test3",
    "password": "pass_test3"
}

# =========================================================================================
old_pass_data = loaded_data["loaded"]
new_password = {
    "username" : "username2",
    "password" : "password2"
}

new_old_password = {
    "username" : "username3",
    "password" : "password3"
}

# Add to "data"
old_data_list.insert(0, new_data)
old_data_list.insert(0, new_new_data)
old_data_list.insert(0, new_old_data)
# Add to "login"
old_pass_data.insert(0, new_password)
old_pass_data.insert(0, new_old_password)
# Update
loaded_data.update({"data": old_data_list, "loaded": old_pass_data})

with open(new_file, "w") as json_file:
    json.dump(loaded_data, json_file, indent=4)
import json
import os
import random
import time

path = 'Players' #Folder to store all player's info
if not os.path.exists(path):
    os.makedirs(path)

def login(): #Validate login of the user/ player
    question = input("Do you have an account? y/n: ")
    if question.lower() == 'n':
        signup() #Triggers the signup function if the player does not have an account
    elif question.lower() == "y":
        print("Please enter your account information")
        username = input("Username: ")
        password = input("Password: ")
        try:
            with open(os.path.join(path, username + ".json"), "r") as game: #Opens the file associated to the player
                info = json.load(game)
            if info["username"] == username and info["password"] == password: #Validates information before opening the player's file
                os.system("clear")
                print("\nUsername: ", username.title() + " validated!")
                time.sleep(3)
                os.system("clear")
                with open("current_player.json", "w") as file: #Loads the validated player's file to current player
                    json.dump(info, file)
            else:
                print("Incorrect username or password")
                login()
        except FileNotFoundError:
            print("We can not find that account\n Please try again")
            login()        
        
def signup(): #Function to allow new players to create an account
    print("Welcome to Sudbury Hunt! Sign up for an account!")
    name = input(str("Please enter your name: "))
    username = input("Please select a username: ")
    password = input("Please choose a password: ")
    
    data = {}
    data["name"] = name
    data["username"] = username
    data["password"] = password 
    data["progress"] = 0
    data["health"] = 100
    data["balance"] = random.randint(100,200)
    
    with open(os.path.join(path, username + ".json"), "w") as infile:
        data = json.dump(data, infile)
    print("\nSuccess! Enter your detail again.")
    print("\n")
    login()

login()
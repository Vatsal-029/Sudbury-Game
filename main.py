import login_info #Initiates the login process
import json
import time
import requests
import random
import sys
import os
from art import *
from termcolor import colored, cprint

path = 'Players' #player data in this folder
if not os.path.exists(path):
  os.makedirs(path)

with open("current_player.json", "r") as game: #Loads the current player data after validating the login
    data = json.load(game)

username = data["username"]
name = data["name"].capitalize()
health = data["health"]
money = data["balance"]
room = data["progress"]

def typewriter_effect(words, speed): #Function to perform typewriter text effect, conditions accept string and speed of the effect
  for char in words:
      time.sleep(speed)
      sys.stdout.write(char)
      sys.stdout.flush()

tprint("Welcome to the 'Sudbury' Hunt", font = "small") #Fancy text to print
tprint(f"{name} !!", font="small")
tprint("Lets find the Diamond!!", font = "small")
time.sleep(5)
os.system("clear") #Clears the console screen

url_data = "https://raw.githubusercontent.com/Vatsal-029/Sudbury-Game/main/map_sudbury.json" #Api to extract main game data
request_data = requests.get(url_data)
response = request_data.json()

city = "sudbury" #City is Sudbury by default since the game revolves around the city
api = "1ce511b679f21c8147422babcbeb5656"
weather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
request_info = requests.get(weather)
response_weather = request_info.json()
current_weather = response_weather['weather'][0]['description'].capitalize()
#Uses the weather info to give the user/ player a sense of the weather around (if in Sudbury) while playing the game

while True:
  print(f"Current Location: {response[room]['name']}, {city.capitalize()} |\t Health: {health}% |\t Money Left: ${money} |\t Current Weather: {current_weather} |\n") #Prints the current room progress, health, money, and weather information when the player is playing 
  
  typewriter_effect(response[room]["story"], 0.08)
  print("\n")
  
  if response[room]["stranger"] == 1: #Conditions when the player meets a stranger in their room
    typewriter_effect("The stranger introduces himself.\n", 0.08)
    import stranger #Initiates the stranger.py file
    time.sleep(3)
    typewriter_effect("And he whispers you the locations!\n", 0.08)

  if response[room]["tip"] == 1: #Conditions when the player meets a person who demands money in exchange of the information
    price = random.randint(10,20)
    typewriter_effect(f"Some advice comes with a price! For this you paid {price}\n", 0.05)
    money = money - price
    
  if response[room]["win"] == 1: #Conditions when the player reaches the winning room
    typewriter_effect("You found the Diamond! Winner!\n", 0.05)
    jackpot = random.randint(5000,10000) #Reward for winning the game
    money = money + jackpot
    typewriter_effect(f"You won ${jackpot}, and now have a total of ${money}\n \n", 0.1)
    sys.exit("Thanks for playing!")
    
  elif response[room]["lose"] == 1: #Conditions when the player reaches the losing room 
    typewriter_effect("Game Over!\n", 0.3)
    health = health - random.randint(5,15) #Punishment for losing
    sys.exit("Thanks for playing!")

  cprint(response[room]["nav"],"yellow") #Print's output in yellow color
  choice = input("\nSelect any one of the options: ")
  
  current_room = response[room]["id"] #captures information on the current room while playing
  current_money = money #captures information on the current money while playing
  current_health = health
  new_data = data
  new_data.update({"progress":current_room, "health":current_health, "balance":current_money}) #updates information in the json file

  with open("current_player.json", "w+") as jsonFile: #loads the updated information to current_player information
      json.dump(new_data, jsonFile)
  
  with open(os.path.join(path, username + ".json"), "w+") as jsonFile: #also loads the updated information to player's json information
      json.dump(new_data, jsonFile)
  
  #Movements in the room according to the user choice
  if choice == '1': 
      room = response[room]["c1"] - 1
  elif choice == '2':
      room = response[room]["c2"] - 1
  elif choice == '3':
      room = response[room]["c3"] - 1
  elif choice == '4':
      sys.exit("Thanks for playing the game! Goodbye.")
  else:
      print("Pleae make a valid choice")

  time.sleep(2)
  os.system("clear")
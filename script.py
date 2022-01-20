# import json
# import random
import re
import time

# from inputs import *
from rich.console import Console
from selenium import webdriver

# import pandas as pd
# import requests

# import webbrowser

# import katan_ai

console = Console()

driver_path = "?????????????????????"

url = "https://colonist.io/?#"

driver = webdriver.Chrome("{}".format(driver_path))  # in inputs file
driver.get("{}".format(url))
start_game_button = driver.find_element_by_class_name("btn_create")

console.log("page is loading")
time.sleep(15)


console.log("entering the game")
start_game_button.send_keys("\n")


time.sleep(5)

console.log("this is the game id")
console.log(driver.current_url)
game_url = driver.current_url

console.log("making the game private")
private_game_button = driver.find_element_by_id("room_center_checkbox_privategame")
time.sleep(3)
private_game_button.click()
console.log("made the game private")


# getting how many users are in the game
players = driver.find_element_by_id("lobby_userlist_header")
players_text = players.text
int_players_in_game = int(re.search(r"\d+", players_text).group())
i = 0
# while player count is less than one, stay as the leader for 2 minutes - after that end the game.
while int_players_in_game <= 1:
    time.sleep(2)
    players_loop = driver.find_element_by_id("lobby_userlist_header")
    players_text_loop = players_loop.text
    int_players_in_game = int(re.search(r"\d+", players_text_loop).group())
    i = i + 1
    if i == 60:
        console.log("No-one has entered the game. Shutting it down.")
        break


console.log("leaving the game")

# this quits the game, which transfers the ownership of the room to the next user, or kills the lobby
time.sleep(2)
driver.quit()
exit(0)

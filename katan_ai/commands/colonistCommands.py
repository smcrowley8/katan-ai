"""Handles commands for interacting with colonist.io katan game"""
# import json
# import random
# import re
# from inputs import *

# from selenium import webdriver
# from selenium.webdriver.common.by import By

import time

import selenium

from katan_ai.commands.constants import CHROMEDRIVER_PATH, COLONIST_URL

# import pandas as pd
# import requests


def command_join_lobby(lobbyID: str) -> None:
    """Joins a colonist.io katan lobby based on ID"""
    browser = selenium.webdriver.Chrome(CHROMEDRIVER_PATH)
    browser.get(COLONIST_URL + lobbyID)
    time.sleep(2)

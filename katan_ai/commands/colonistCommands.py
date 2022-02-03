"""Handles commands for interacting with colonist.io katan game"""
# import json
# import random
# import re
# from inputs import *
# import time

from rich.console import Console
from selenium import webdriver
from selenium.webdriver.common.by import By

from .constants import CHROMEDRIVER_PATH, COLONIST_URL

# import pandas as pd
# import requests


console = Console()


def command_join_lobby(lobbyID: str) -> None:
    """Joins a colonist.io katan lobby based on ID"""
    browser = webdriver.Chrome(CHROMEDRIVER_PATH)
    browser.get(COLONIST_URL + lobbyID)

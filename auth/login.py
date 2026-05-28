from structure import Player
from utils import get_player

def login(x):
    username = input("Input your username: ")
    password = input("Input your password: ")

    if not username in x or x[username] != password:
        print("Invalid username or password submited")
        return

    stats = get_player(username)
    return Player(username, **stats)
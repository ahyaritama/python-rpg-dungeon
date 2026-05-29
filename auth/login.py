from structure import Player
from utils import get_player

def login(x):
    username = input("Input your username: ")
    password = input("Input your password: ")

    if not username in x or x[username] != password:
        print("Invalid username or password submited\n")
        return

    stats = get_player(username)
    print(f"Successfully login using account {username}\n")
    return Player(username, **stats)
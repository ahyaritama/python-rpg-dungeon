from ..inventory.inventory import Inventory
from ..struct.player import Player
from ..util.auth import (
    add_player,
    validate
)

def register(players: dict[str, str]):
    while True:
        username = input("Input your username: ")
        if username in players:
            print("[*] Username already taken\n")
            continue
        
        password = input("Input your password: ")
        ok, msg = validate(username, password)
        if ok:
            players[username] = password
            break
        print(msg)

    stats = add_player(username, password)
    print(f"Successfully create account {username}\n")
    return Player(username, stats, None, Inventory())
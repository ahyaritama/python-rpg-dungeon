from ..inventory import Equipment, Inventory
from ..struct import Player
from ..util import (
    add_player,
    validate
)

def register(players: dict[str, str]):
    print("\n(Use CTRL + C to quit)")
    while True:
        try:
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
        except KeyboardInterrupt:
            return

    equipment = Equipment(set(), set())
    bag = Inventory()
    skill: set[str] = set()
    stats, rooms = add_player(username, password)

    print(f"Successfully create account {username}\n")
    return Player(username, stats, skill, bag, equipment, rooms)
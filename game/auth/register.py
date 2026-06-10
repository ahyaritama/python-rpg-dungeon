# from ..inventory import Equipment, Inventory
# from ..struct import Player
# from ..util import add_player, validate

from ..const import DEFAULT_STATS, DEFAULT_POSITION
from ..struct import Equipment, Inventory, Player
from ..struct.player import PlayerDict
from ..util import add_player, validate

def register(player_dict: PlayerDict) -> Player | None:
    print("\n(Use CTRL + C to quit)")
    while True:
        try:
            username = input("Input your username: ")
            if username in player_dict:
                print("[*] Username already taken\n")
                continue
            
            password = input("Input your password: ")
            ok, msg = validate(username, password)
            if ok:
                player_dict[username] = password
                break
            print(msg)
        except KeyboardInterrupt:
            return
    
    add_player(username, password)
    equipment = Equipment(set(), set())
    inventory = Inventory()
    rooms_tup = (DEFAULT_POSITION, list(), set())
    skill_set = set()
    stats_dict = DEFAULT_STATS.copy()

    print(f"Successfully create account {username}\n")
    return Player(username, stats_dict, inventory, equipment, skill_set, rooms_tup)

    # equipment = Equipment(set(), set())
#     bag = Inventory()
#     skill: set[str] = set()
#     stats, rooms = add_player(username, password)

#     print(f"Successfully create account {username}\n")
#     return Player(username, stats, skill, bag, equipment, rooms)

# def register(players: dict[str, str]):
#     print("\n(Use CTRL + C to quit)")
#     while True:
#         try:
#             username = input("Input your username: ")
#             if username in players:
#                 print("[*] Username already taken\n")
#                 continue
            
#             password = input("Input your password: ")
#             ok, msg = validate(username, password)
#             if ok:
#                 players[username] = password
#                 break
#             print(msg)
#         except KeyboardInterrupt:
#             return

#     equipment = Equipment(set(), set())
#     bag = Inventory()
#     skill: set[str] = set()
#     stats, rooms = add_player(username, password)

#     print(f"Successfully create account {username}\n")
#     return Player(username, stats, skill, bag, equipment, rooms)
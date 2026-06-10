# from ..inventory import Item
# from ..struct import Player
# from ..util import (
#     get_player_equipment,
#     get_player_items,
#     get_player_rooms,
#     get_player_skills,
#     get_player_stats
# )

from ..struct import (
    Equipment,
    Inventory,
    Player,
)
from ..struct.item import ItemDict
from ..struct.player import PlayerDict
from ..util import (
    get_player_equipment,
    get_player_items,
    get_player_rooms,
    get_player_skills,
    get_player_stats
)

def login(player_dict: PlayerDict, item_dict: ItemDict) -> Player | None:
    print("\n(Use CTRL + C to quit)")
    while True:
        try:
            username = input("Input your username: ")
            password = input("Input your password: ")

            if username in player_dict:
                if player_dict[username] == password:
                    break
            
            print("Invalid username or password submited\n")
        except KeyboardInterrupt:
            return
    
    equip_set = get_player_equipment(username)
    equip_item_set = {item_dict[code] for code in equip_set}
    equipment = Equipment(equip_set, equip_item_set)

    item_list = get_player_items(username)
    inventory = Inventory()
    for code, qty in item_list:
        inventory.insert(item_dict[code], qty)

    rooms_tup = get_player_rooms(username)
    skill_set = get_player_skills(username)
    stats_dict = get_player_stats(username)
    
    print(f"Successfully login using account {username}\n")
    return Player(username, stats_dict, inventory, equipment, skill_set, rooms_tup)
    




# def login(players: dict[str, str], items: dict[str, Item]):
#     print("\n(Use CTRL + C to quit)")
#     while True:
#         try:
#             username = input("Input your username: ")
#             password = input("Input your password: ")

#             if (username in players and players[username] == password):
#                 break
            
#             print("Invalid username or password submited\n")
#         except KeyboardInterrupt:
#             return

#     equipment = get_player_equipment(username, items)
#     p_items = get_player_items(username, items)
#     rooms = get_player_rooms(username)
#     skills = get_player_skills(username)
#     stats = get_player_stats(username)

#     print(f"Successfully login using account {username}\n")
#     return Player(username, stats, skills, p_items, equipment, rooms)
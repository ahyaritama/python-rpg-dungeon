from .battle import start_battle
from .stats import show_stats

from ..struct import Map, Player, Room
from ..struct.skill import SkillList
from ..util import (
    create_header,
    set_player_items,
    set_player_rooms
)

def explore(player: Player, skill_list: SkillList, dungeon_map: Map):
    """Main handler of explore feature."""
    while True:
        header_len = create_header(player.name, player.money, "EXPLORE")
        print("Well adventurers, it looks like")
        print("you can't wait to explore this")
        print("dungeon.")
        print("-" * header_len)

        _check_room_handler(player, dungeon_map)
        print("=" * header_len)
        options = _build_menu_option(player, skill_list, dungeon_map)
        choice = input("Your Choice: ")
        try:
            result = options[choice]()
            if result is True:
                _clear_room(player, dungeon_map.graph[player.position][0])
        except KeyError:
            break



# PRIVATE FUNCTION
def _build_menu_option(player: Player, skill_list: SkillList, dungeon_map: Map):
    """Build and print available option in
    player's position and return dictionary
    with callable as the value.
    """
    print("[0] Show Rooms")
    options = {"0": lambda: _show_room_handler(player, dungeon_map)}
    if not player.is_room_cleared(player.position):
        monster = dungeon_map.graph[player.position][0].monster
        print("[1] View Stats")
        print("[2] Fight")
        if not player.move_list.is_empty():
            last_position = str(player.move_list.pop())
            print("[3] Back")
            options["3"] = lambda: player.set_position(last_position)

        options["1"] = lambda: show_stats(player)
        options["2"] = lambda: start_battle(player, monster, skill_list)  # type: ignore
    else:
        rooms = dungeon_map.graph[player.position][1]
        for i in range(len(rooms)):
            print(f"[{i + 1}] {rooms[i].name}")
            options[str(i + 1)] = lambda c=i: _set_player_position(player, rooms[c].name)
    print("[*] Main Menu")
    return options

def _check_room_handler(player: Player, dungeon_map: Map):
    """Check if monster in this room already
    defeated. After defeated, player can explore
    another room.
    """
    print(f"Your position: {player.position}")
    if not player.is_room_cleared(player.position):
        monster = dungeon_map.graph[player.position][0].monster
        print("There is a monster waiting for")
        print("you in this room.\n")
        print(f"Name      : {monster.name}")
        print(f"Max HP    : {monster.stats["Max HP"]}")
        print(f"ATK       : {monster.stats["ATK"]}")
        print(f"DEF       : {monster.stats["DEF"]}")
        print(f"Exp Drop  : {monster.exp_drop}")
        print(f"Coin Drop : {monster.coin_drop}")
    else:
        print("You have defeated the monster")
        print("in this room. You can explore")
        print("the other rooms.")
    
def _clear_room(player: Player, room: Room):
    """Mark this room as clear, take
    items from this room and save it to
    player's items storage.
    """
    if len(room.item_list) > 0:
        header_len = create_header(player.name, player.money, "EXPLORE")
        print("You find these items in the room:")
        for x in room.item_list:
            player.inventory.insert(x, 1)
            set_player_items(player.name, player.get_items())
            print(f"    - {x.name} X 1")
        print("=" * header_len)
        input("[OK]")

    player.clear_room(room.name)
    set_player_rooms(player.name, player.get_rooms())

def _set_player_position(player: Player, room_name: str):
    """Set player's new position and
    add old position to move stack.
    """
    player.move_list.push(player.position)
    player.set_position(room_name)

def _show_room_handler(player: Player, dungeon_map: Map):
    """Show all rooms and all connected rooms"""
    header_len = create_header(player.name, player.money, "EXPLORE")
    dungeon_map.display_room()
    print("=" * header_len) 
    input("[Back]")
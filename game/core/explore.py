from .battle import start_battle
from .stats import show_stats

from ..util import clear_screen, set_player_items, set_player_rooms

from ..struct import (
    Player,
    Room,
    SkillTree,
    Map
)

def explore(player: Player, skill_tree: SkillTree, dungeon_map: Map):
    while True:
        clear_screen()
        header = "=" * 12 + " EXPLORE " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        print("Well adventurers, it looks like")
        print("you can't wait to explore this")
        print("dungeon.")
        print("-" * len(header))

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
                
        print("=" * len(header))

        options: dict[str, str] = {}
        if not player.is_room_cleared(player.position):
            print("[1] View Stats")
            print("[2] Fight")
            options["1"] = lambda: show_stats(player)
            options["2"] = lambda: start_battle(player, monster)
        else:
            rooms = dungeon_map.graph[player.position][1]
            for i in range(len(rooms)):
                print(f"[{i + 1}] {rooms[i].name}")
                options[str(i + 1)] = lambda c=i: player.set_position(rooms[c].name)

        print("[*] Main Menu")
        choice = input("Your Choice: ")

        try:
            result = options[choice]()
            if result is True:
                _clear_room(player, dungeon_map.graph[player.position][0])
        except KeyError:
            break


# PRIVATE FUNCTION
def _clear_room(player: Player, room: Room):
    if len(room.items) > 0:
        clear_screen()
        header = "=" * 12 + " EXPLORE " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        print("You find these items in the room:")
        for x in room.items:
            player.bag.insert(x, 1)
            set_player_items(player.name, player.bag)
            print(f"    - {x.name} X 1")

        print("=" * len(header))
        input("[OK]")

    player.clear_room(room.name)
    print(player.cleared)
    set_player_rooms(player.name, player.position, player.cleared)
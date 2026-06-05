from.explore import explore
from .inventory import show_inventory
from .skills import show_skills
from .stats import show_stats

from ..struct import (
    Player,
    SkillTree,
    Map
)
from ..util import clear_screen

def main_menu(player: Player, skill_tree: SkillTree, dungeon_map: Map):
    while True:
        clear_screen()
        header = "=" * 12 + " MAIN MENU " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)
    
        print("Welcome adventurer!")
        print("Here you can choose anything")
        print("from the available menus.")

        print("=" * len(header))
        print("[1] View Stats")
        print("[2] Explore")
        print("[3] Skills")
        print("[4] Inventory")
        print("[*] Logout")

        choice = input("Your Choice: ")
        match choice:
            case "1":
                show_stats(player)
            case "2":
                explore(player, skill_tree.in_order(), dungeon_map)
            case "3":
                show_skills(player, skill_tree)
            case "4":
                show_inventory(player)
            case _:
                print("Logging Out...\n")
                break
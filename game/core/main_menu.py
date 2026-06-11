from.explore import explore
from .inventory import Item, show_inventory
from .reset import reset_progress
from .shop import show_shop
from .skills import show_skills
from .stats import show_stats

from ..struct import (
    Player,
    SkillTree,
    Map
)
from ..util import create_header

def main_menu(player: Player, items: dict[str, Item], skill_tree: SkillTree, dungeon_map: Map):
    """Main menu handler."""
    while True:
        header_len = create_header(player.name, player.money, "MAIN MENU")
    
        print("Welcome adventurer!")
        print("Here you can choose anything")
        print("from the available menus.")

        print("=" * header_len)
        print("[1] View Stats")
        print("[2] Explore")
        print("[3] Skills")
        print("[4] Inventory")
        print("[5] Shop")
        print("[6] Reset Progress")
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
            case "5":
                show_shop(player, items)
            case "6":
                reset_progress(player)
            case _:
                print("Logging Out...\n")
                break
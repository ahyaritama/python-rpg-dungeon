from .inventory import show_inventory
from .stats import show_stats

from ..struct import Player
from ..util import clear_screen

def main_menu(player: Player):
    while True:
        clear_screen()
        header = "=" * 12 + " MAIN MENU " + "=" * 12

        print(f"{'Name':<8}: {player.name}")
        print(f"{'Balance':<8}: {player.money}")
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
                pass
            case "3":
                pass
            case "4":
                show_inventory(player)
            case _:
                print("Logging Out...\n")
                break
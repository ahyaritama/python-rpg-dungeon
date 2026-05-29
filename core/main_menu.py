import utils
from .stats import stats
from structure.player import Player

def main_menu(player: Player):
    while True:
        utils.clear_screen()
        header = "=" * 10 + " MAIN MENU " + "=" * 10

        print(f"{'Name':<8}: {player.name}")
        print(f"{'Balance':<8}: {player.money}")
        print(header)
    
        print("Welcome adventurer!")
        print("Here you can choose anything")
        print("from the available menus.")

        print("=" * len(header))
        print("[1] View Stats")
        print("[2] Explore")
        print("[3] Inventory")
        print("[*] Logout")

        choice = input("Your Choice: ")
        match choice:
            case "1":
                stats(player)
            case "2":
                pass
            case "3":
                pass
            case _:
                print("Logging Out...\n")
                break
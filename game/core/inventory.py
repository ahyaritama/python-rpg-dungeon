from ..inventory import Inventory, InventoryItem
from ..struct.player import Player
from ..util.view import clear_screen

def show_inventory(player: Player):
    while True:
        clear_screen()
        header = "=" * 10 + " INVENTORY " + "=" * 10

        print(f"{'Name':<8}: {player.name}")
        print(f"{'Balance':<8}: {player.money}")
        print(header)

        print("Here you can see the items")
        print("you have and can use.")

        print("=" * len(header))
        print("[1] Show All")
        print("[2] Browse")
        print("[*] Back")

        choice = input("Your Choice: ")
        match choice:
            case "1":
                _show_all(player)
            case "2":
                _browse(player, player.bag.head)
            case _:
                break
    pass


# PRIVATE FUNCTION
def _browse(player: Player, node: InventoryItem, ok=False):
    while True:
        clear_screen()
        header = "=" * 10 + " INVENTORY " + "=" * 10

        print(f"{'Name':<8}: {player.name}")
        print(f"{'Balance':<8}: {player.money}")
        print(header)

        if not node:
            print("No items found!")
            print("=" * len(header))

            input("[Back]")
            return ok
        
        print(f"{'Name':<7}: {node.data.name}")
        print(f"{'Effect':<7}: {str(node.data.code).split("_", 1)[0]} +{node.data.effect}")
        print(f"{'Price':<7}: {node.data.price}")
        print(f"{'Qty':<7}: {node.qty}")

        print("=" * len(header))
        print("[1] Prev Item")
        print("[2] Next Item")
        print("[3] Use Item")
        print("[4] Sell Item")
        print("[5] Back")
        print("[*] Inventory")

        choice = input("Your Choice: ")
        match choice:
            case "1":
                ok = _browse(player, node.prev, True)
            case "2":
                ok = _browse(player, node.next, True)
            case "3":
                return True
            case "4":
                return True
            case "5":
                return True
            case _:
                return False
            
        if not ok:
            return False


def _show_all(player: Player):
    clear_screen()
    header = "=" * 10 + " INVENTORY " + "=" * 10

    print(f"{'Name':<8}: {player.name}")
    print(f"{'Balance':<8}: {player.money}")
    print(header)

    print("=" * len(header))
    input("[Back]")
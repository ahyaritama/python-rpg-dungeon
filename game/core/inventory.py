from ..inventory import Inventory, InventoryItem
from ..struct import Player
from ..util import clear_screen

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
                player.equip(node.data)
                if node.qty == 0:
                    player.bag.delete(node.data)
                    return True
                continue
            case "4":
                player.money += node.data.price
                node.qty -= 1
                print(f"Successfully sell {node.data.name}")
                if node.qty == 0:
                    player.bag.delete(node.data)
                    return True
                continue
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

    current = player.bag.head
    table_head = f"| {'Name':^11} | {'Code':^6} | {'Qty.':^4} |"
    print(f"{table_head}\n{'-' * len(table_head)}")
    while current:
        print(f"| {current.data.name:<11} | {current.data.code:<6} | {current.qty:<4} |")
        current = current.next

    print("=" * len(header))
    input("[Back]")
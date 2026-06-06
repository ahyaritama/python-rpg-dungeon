from ..inventory import InventoryItem, Item
from ..struct import Player
from ..util import (
    clear_screen,
    set_player_items,
    set_player_stats
)

def show_inventory(player: Player):
    while True:
        clear_screen()
        header = "=" * 12 + " INVENTORY " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        print("Here you can see the items")
        print("you have and can use.")

        print("=" * len(header))
        print("[1] Show All")
        print("[2] Browse")
        print("[3] Search")
        print("[*] Back")

        choice = input("Your Choice: ")
        match choice:
            case "1":
                _show_all(player)
            case "2":
                _browse(player, player.bag.head)
            case "3":
                _search(player)
            case _:
                break
    pass


# PRIVATE FUNCTION
def _browse(player: Player, node: InventoryItem, ok=False):
    while True:
        clear_screen()
        header = "=" * 12 + " INVENTORY " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        if not node:
            print("No items found!")
            print("=" * len(header))

            input("[Back]")
            return ok
        
        print(f"{'Name   '}: {node.data.name}")
        print(f"{'Code   '}: {node.data.code}")
        print(f"{'Effect '}: {str(node.data.code).split("_", 1)[0]} +{node.data.effect}")
        print(f"{'Price  '}: {node.data.price}")
        print(f"{'Qty    '}: {node.qty}")

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
                ok, msg = player.equip(node.data)
                set_player_stats(player)
                print(msg)
                input("[OK]")
                if ok is False:
                    continue
                
                node.qty -= 1
                if node.qty <= 0:
                    player.bag.delete(node.data)
                    set_player_items(player.name, player.bag)
                    return True
                set_player_items(player.name, player.bag)
                continue
            case "4":
                player.money += node.data.price
                set_player_stats(player)
                print(f"Successfully sell {node.data.name}")
                input("[OK]")

                node.qty -= 1
                if node.qty <= 0:
                    player.bag.delete(node.data)
                    set_player_items(player.name, player.bag)
                    return True
                set_player_items(player.name, player.bag)
                continue
            case "5":
                return True
            case _:
                return False
            
        if not ok:
            return False

def _search(player: Player):
    while True:
        clear_screen()
        header = "=" * 12 + " INVENTORY " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        print("Here you can search")
        print("items by name or code.")

        print("=" * len(header))
        print("[1] Search by Code")
        print("[2] Search by Name")
        print("[*] Back")
        
        choice = input("Your Choice: ")
        match choice:
            case "1":
                print("-" * len(header))
                choice = input("Input Item's Code: ")
                _show_item(player, player.bag.search_by_code(choice))
            case "2":
                print("-" * len(header))
                choice = input("Input Item's Name: ")
                _show_item(player, player.bag.search_by_name(choice))
            case _:
                break
        

def _show_all(player: Player):
    while True:
        clear_screen()
        header = "=" * 12 + " INVENTORY " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        current = player.bag.head
        table_head = f"| {'Name':^15} | {'Code':^6} | {'Qty.':^4} |"
        print(f"{table_head}\n{'-' * len(table_head)}")
        while current:
            print(f"| {current.data.name:<15} | {current.data.code:<6} | {current.qty:<4} |")
            current = current.next

        print("=" * len(header))
        print("[1] Sort by Code")
        print("[2] Sort by Name")
        print("[3] Sort by Price")
        print("[*] Back")

        choice = input("Your Choice: ")
        match choice:
            case "1":
                print("-" * len(header))
                print("[1] Descending")
                print("[*] Ascending")
                choice = input("Your Choice: ")
                match choice:
                    case "1":
                        player.bag.sort_by_code(False)
                    case _:
                        player.bag.sort_by_code()
            case "2":
                print("" + "-" * len(header))
                print("[1] Descending")
                print("[*] Ascending")
                choice = input("Your Choice: ")
                match choice:
                    case "1":
                        player.bag.sort_by_name(False)
                    case _:
                        player.bag.sort_by_name()
            case "3":
                print("" + "-" * len(header))
                print("[1] Descending")
                print("[*] Ascending")
                choice = input("Your Choice: ")
                match choice:
                    case "1":
                        player.bag.sort_by_price(False)
                    case _:
                        player.bag.sort_by_price()
            case _:
                break

def _show_item(player: Player, detail: tuple[Item, int]):
    while True:
        clear_screen()
        header = "=" * 12 + " INVENTORY " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        if detail[0] is None:
            print("Item Not Found!")
            print("=" * len(header))
            input("[Back]")
            break

        item = detail[0]
        qty = detail[1]
            
        print(f"{'Name   '}: {item.name}")
        print(f"{'Code   '}: {item.code}")
        print(f"{'Effect '}: {str(item.code).split("_", 1)[0]} +{item.effect}")
        print(f"{'Price  '}: {item.price}")
        print(f"{'Qty    '}: {qty}")

        print("=" * len(header))
        print("[1] Use Item")
        print("[2] Sell Item")
        print("[*] Back")

        choice = input("Your Choice:")
        match choice:
            case "1":
                ok, msg = player.equip(item.data)
                set_player_stats(player)
                print(msg)
                input("[OK]")
                if ok is False:
                    continue
                
                item.qty -= 1
                if item.qty <= 0:
                    player.bag.delete(item.data)
                    set_player_items(player.name, player.bag)
                    break
                set_player_items(player.name, player.bag)
            case "2":
                player.money += item.data.price
                set_player_stats(player)
                print(f"Successfully sell {item.data.name}")
                input("[OK]")

                item.qty -= 1
                if item.qty <= 0:
                    player.bag.delete(item.data)
                    set_player_items(player.name, player.bag)
                    break
                set_player_items(player.name, player.bag)
            case _:
                break
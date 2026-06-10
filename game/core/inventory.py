# from ..inventory import InventoryItem, Item
# from ..struct import Player
# from ..util import (
#     clear_screen,
#     set_player_items,
#     set_player_stats
# )

from ..struct import Item, Player
from ..struct.inventory import InventoryNode
from ..util import (
    create_header,
    set_player_stats,
    set_player_items
)

def show_inventory(player: Player):
    while True:
        header_len = create_header(player.name, player.money, "INVENTORY")
        print("Here you can see the items")
        print("you have and can use.")
        print("=" * header_len)

        print("[1] Show All")
        print("[2] Browse")
        print("[3] Search")
        print("[*] Back")
        choice = input("Your Choice: ")
        match choice:
            case "1":
                _show_all(player)
            case "2":
                _browse(player, player.inventory.head)
            case "3":
                _search(player)
            case _:
                break
        



# PRIVATE FUNCTION
def _browse(player: Player, node: InventoryNode | None, ok=False):
    while True:
        header_len = create_header(player.name, player.money, "INVENTORY")
        if not node:
            print("No items found!")
            print("=" * header_len)
            input("[Back]")
            return ok

        print("=" * header_len)
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
                ok = _use_item(player, node)
                if ok is None:
                    continue
            case "4":
                ok = _sell_item(player, node)
                if ok is None:
                    continue
            case "5":
                return True
            case _:
                return False
            
        if ok is False:
            return False

def _sell_item(player: Player, node: InventoryNode) -> bool | None:
    player.money += node.data.price
    set_player_stats(player.name, player.get_stats())
    print(f"Successfully sell {node.data.name}")
    input("[OK]")

    ok = _delete_empty_node(player, node)
    if not ok:
        return True
        
def _use_item(player: Player, node: InventoryNode) -> bool | None:
    ok, msg = player.equip(node.data)
    set_player_stats(player.name, player.get_stats())
    print(msg)
    input("[OK]")
    if ok is False:
        return ok
    
    ok = _delete_empty_node(player, node)
    if not ok:
        return True

def _search(player: Player):
    while True:
        header_len = create_header(player.name, player.money, "INVENTORY")
        print("Here you can search")
        print("items by name or code.")
        print("=" * header_len)
        print("[1] Search by Code")
        print("[2] Search by Name")
        print("[*] Back")
        choice = input("Your Choice: ")
        match choice:
            case "1":
                print("-" * header_len)
                choice = input("Input Item's Code: ")
                node = player.inventory.search_by_code(choice)
                if node:
                    _show_item(player, node)
                else:
                    print("Item Not Found!")
                    print("=" * header_len)
                    input("[Back]")
            case "2":
                print("-" * header_len)
                choice = input("Input Item's Name: ")
                node = player.inventory.search_by_name(choice)
                if node:
                    _show_item(player, node)
                else:
                    print("Item Not Found!")
                    print("=" * header_len)
                    input("[Back]")
            case _:
                break
        

def _show_all(player: Player):
    while True:
        header_len = create_header(player.name, player.money, "INVENTORY")
        table_head = f"| {'Name':^15} | {'Code':^6} | {'Qty.':^4} |"
        print(f"{table_head}\n{'-' * len(table_head)}")

        current = player.inventory.head
        while current:
            print(f"| {current.data.name:<15} | {current.data.code:<6} | {current.qty:<4} |")
            current = current.next

        print("=" * header_len)
        print("[1] Sort by Code")
        print("[2] Sort by Name")
        print("[3] Sort by Price")
        print("[*] Back")
        choice = input("Your Choice: ")
        match choice:
            case "1":
                print("-" * header_len)
                print("[1] Descending")
                print("[*] Ascending")
                choice = input("Your Choice: ")
                match choice:
                    case "1":
                        player.inventory.sort_by_code(False)
                    case _:
                        player.inventory.sort_by_code()
            case "2":
                print("" + "-" * header_len)
                print("[1] Descending")
                print("[*] Ascending")
                choice = input("Your Choice: ")
                match choice:
                    case "1":
                        player.inventory.sort_by_name(False)
                    case _:
                        player.inventory.sort_by_name()
            case "3":
                print("" + "-" * header_len)
                print("[1] Descending")
                print("[*] Ascending")
                choice = input("Your Choice: ")
                match choice:
                    case "1":
                        player.inventory.sort_by_price(False)
                    case _:
                        player.inventory.sort_by_price()
            case _:
                break

def _show_item(player: Player, node: InventoryNode):
    while True:
        header_len = create_header(player.name, player.money, "INVENTORY")
        print(f"{'Name   '}: {node.data.name}")
        print(f"{'Code   '}: {node.data.code}")
        print(f"{'Effect '}: {str(node.data.code).split("_", 1)[0]} +{node.data.effect}")
        print(f"{'Price  '}: {node.data.price}")
        print(f"{'Qty    '}: {node.qty}")
        print("=" * header_len)
        print("[1] Use Item")
        print("[2] Sell Item")
        print("[*] Back")

        choice = input("Your Choice:")
        match choice:
            case "1":
                ok, msg = player.equip(node.data)
                set_player_stats(player.name, player.get_stats())
                print(msg)
                input("[OK]")
                if ok is False:
                    continue
                
                ok = _delete_empty_node(player, node)
                if not ok:
                    break
            case "2":
                player.money += node.data.price
                set_player_stats(player.name, player.get_stats())
                print(f"Successfully sell {node.data.name}")
                input("[OK]")
                ok = _delete_empty_node(player, node)
                if not ok:
                    break
            case _:
                break

def _delete_empty_node(player: Player, node: InventoryNode):
    node.qty -= 1
    if node.qty <= 0:
        player.inventory.delete(node.data)
        set_player_items(player.name, player.get_items())
        return False
    set_player_items(player.name, player.get_items())
    return True


# def show_inventory(player: Player):
#     while True:
#         clear_screen()
#         header = "=" * 12 + " INVENTORY " + "=" * 12

#         print(f"{'Name    '}: {player.name}")
#         print(f"{'Balance '}: {player.money}")
#         print(header)

#         print("Here you can see the items")
#         print("you have and can use.")

#         print("=" * header_len)
#         print("[1] Show All")
#         print("[2] Browse")
#         print("[3] Search")
#         print("[*] Back")

#         choice = input("Your Choice: ")
#         match choice:
#             case "1":
#                 _show_all(player)
#             case "2":
#                 _browse(player, player.inventory.head)
#             case "3":
#                 _search(player)
#             case _:
#                 break
#     pass


# # PRIVATE FUNCTION
# def _browse(player: Player, node: InventoryItem, ok=False):
#     while True:
#         clear_screen()
#         header = "=" * 12 + " INVENTORY " + "=" * 12

#         print(f"{'Name    '}: {player.name}")
#         print(f"{'Balance '}: {player.money}")
#         print(header)

#         if not node:
#             print("No items found!")
#             print("=" * header_len)

#             input("[Back]")
#             return ok
        
#         print(f"{'Name   '}: {node.data.name}")
#         print(f"{'Code   '}: {node.data.code}")
#         print(f"{'Effect '}: {str(node.data.code).split("_", 1)[0]} +{node.data.effect}")
#         print(f"{'Price  '}: {node.data.price}")
#         print(f"{'Qty    '}: {node.qty}")

#         print("=" * header_len)
#         print("[1] Prev Item")
#         print("[2] Next Item")
#         print("[3] Use Item")
#         print("[4] Sell Item")
#         print("[5] Back")
#         print("[*] Inventory")

#         choice = input("Your Choice: ")
#         match choice:
#             case "1":
#                 ok = _browse(player, node.prev, True)
#             case "2":
#                 ok = _browse(player, node.next, True)
#             case "3":
#                 ok, msg = player.equip(node.data)
#                 set_player_stats(player)
#                 print(msg)
#                 input("[OK]")
#                 if ok is False:
#                     continue
                
#                 node.qty -= 1
#                 if node.qty <= 0:
#                     player.inventory.delete(node.data)
#                     set_player_items(player.name, player.inventory)
#                     return True
#                 set_player_items(player.name, player.inventory)
#                 continue
#             case "4":
#                 player.money += node.data.price
#                 set_player_stats(player)
#                 print(f"Successfully sell {node.data.name}")
#                 input("[OK]")

#                 node.qty -= 1
#                 if node.qty <= 0:
#                     player.inventory.delete(node.data)
#                     set_player_items(player.name, player.inventory)
#                     return True
#                 set_player_items(player.name, player.inventory)
#                 continue
#             case "5":
#                 return True
#             case _:
#                 return False
            
#         if not ok:
#             return False

# def _search(player: Player):
#     while True:
#         clear_screen()
#         header = "=" * 12 + " INVENTORY " + "=" * 12

#         print(f"{'Name    '}: {player.name}")
#         print(f"{'Balance '}: {player.money}")
#         print(header)

#         print("Here you can search")
#         print("items by name or code.")

#         print("=" * header_len)
#         print("[1] Search by Code")
#         print("[2] Search by Name")
#         print("[*] Back")
        
#         choice = input("Your Choice: ")
#         match choice:
#             case "1":
#                 print("-" * header_len)
#                 choice = input("Input Item's Code: ")
#                 _show_item(player, player.inventory.search_by_code(choice))
#             case "2":
#                 print("-" * header_len)
#                 choice = input("Input Item's Name: ")
#                 _show_item(player, player.inventory.search_by_name(choice))
#             case _:
#                 break
        

# def _show_all(player: Player):
#     while True:
#         clear_screen()
#         header = "=" * 12 + " INVENTORY " + "=" * 12

#         print(f"{'Name    '}: {player.name}")
#         print(f"{'Balance '}: {player.money}")
#         print(header)

#         current = player.inventory.head
#         table_head = f"| {'Name':^15} | {'Code':^6} | {'Qty.':^4} |"
#         print(f"{table_head}\n{'-' * len(table_head)}")
#         while current:
#             print(f"| {current.data.name:<15} | {current.data.code:<6} | {current.qty:<4} |")
#             current = current.next

#         print("=" * header_len)
#         print("[1] Sort by Code")
#         print("[2] Sort by Name")
#         print("[3] Sort by Price")
#         print("[*] Back")

#         choice = input("Your Choice: ")
#         match choice:
#             case "1":
#                 print("-" * header_len)
#                 print("[1] Descending")
#                 print("[*] Ascending")
#                 choice = input("Your Choice: ")
#                 match choice:
#                     case "1":
#                         player.inventory.sort_by_code(False)
#                     case _:
#                         player.inventory.sort_by_code()
#             case "2":
#                 print("" + "-" * header_len)
#                 print("[1] Descending")
#                 print("[*] Ascending")
#                 choice = input("Your Choice: ")
#                 match choice:
#                     case "1":
#                         player.inventory.sort_by_name(False)
#                     case _:
#                         player.inventory.sort_by_name()
#             case "3":
#                 print("" + "-" * header_len)
#                 print("[1] Descending")
#                 print("[*] Ascending")
#                 choice = input("Your Choice: ")
#                 match choice:
#                     case "1":
#                         player.inventory.sort_by_price(False)
#                     case _:
#                         player.inventory.sort_by_price()
#             case _:
#                 break

# def _show_item(player: Player, detail: tuple[Item, int]):
#     while True:
#         clear_screen()
#         header = "=" * 12 + " INVENTORY " + "=" * 12

#         print(f"{'Name    '}: {player.name}")
#         print(f"{'Balance '}: {player.money}")
#         print(header)

#         if detail[0] is None:
#             print("Item Not Found!")
#             print("=" * header_len)
#             input("[Back]")
#             break

#         item = detail[0]
#         qty = detail[1]
            
#         print(f"{'Name   '}: {item.name}")
#         print(f"{'Code   '}: {item.code}")
#         print(f"{'Effect '}: {str(item.code).split("_", 1)[0]} +{item.effect}")
#         print(f"{'Price  '}: {item.price}")
#         print(f"{'Qty    '}: {qty}")

#         print("=" * header_len)
#         print("[1] Use Item")
#         print("[2] Sell Item")
#         print("[*] Back")

#         choice = input("Your Choice:")
#         match choice:
#             case "1":
#                 ok, msg = player.equip(item.data)
#                 set_player_stats(player)
#                 print(msg)
#                 input("[OK]")
#                 if ok is False:
#                     continue
                
#                 item.qty -= 1
#                 if item.qty <= 0:
#                     player.inventory.delete(item.data)
#                     set_player_items(player.name, player.inventory)
#                     break
#                 set_player_items(player.name, player.inventory)
#             case "2":
#                 player.money += item.data.price
#                 set_player_stats(player)
#                 print(f"Successfully sell {item.data.name}")
#                 input("[OK]")

#                 item.qty -= 1
#                 if item.qty <= 0:
#                     player.inventory.delete(item.data)
#                     set_player_items(player.name, player.inventory)
#                     break
#                 set_player_items(player.name, player.inventory)
#             case _:
#                 break
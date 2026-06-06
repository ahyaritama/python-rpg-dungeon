from ..inventory import Item
from ..struct import Player, ShopStack
from ..util import clear_screen, set_player_items, set_player_stats

def show_shop(player: Player, items: dict[str, Item]):
    shop_stack = ShopStack()

    while True:
        clear_screen()
        header = "=" * 12 + " SHOP " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        print("Here you can purchase items.")
        print("Select an item to add to your")
        print("cart.\n")

        codes: dict[str, str] = {}
        for i, item in enumerate(items.values(), 1):
            codes[str(i)] = item.code
            print(f"{f'[{i}]':<4} {item.name:<14} ({item.price:<3} Gold)")

        print("=" * len(header))
        print("[0] Pay")
        print("[*] Back")

        choice = input("Your Choice: ")
        match choice:
            case "0":
                _pay(player, shop_stack)
            case _:
                try:
                    selected_item = items[codes[choice]]
                    print("\n" + shop_stack.enqueue(selected_item))
                    input("[OK]")
                except KeyError:
                    break


# PRIVATE FUNCTION
def _pay(player: Player, stack: ShopStack):
    clear_screen()
    header = "=" * 12 + " SHOP " + "=" * 12

    print(f"{'Name    '}: {player.name}")
    print(f"{'Balance '}: {player.money}")
    print(header)

    if stack.is_empty():
        print("Nothing to pay")
        print("=" * len(header))
        input("[OK]")
        return

    while True:
        item = stack.dequeue()
        if item is None:
            break

        if item.price > player.money:
            print(f"Not enough money to buy {item.name}.")
            break

        player.bag.insert(item, 1)
        player.money -= item.price
        set_player_items(player.name, player.bag)
        set_player_stats(player)
        print(f"Buying {item.name:<14} -{item.price}")
    
    print("=" * len(header))
    input("[OK]")
from ..struct import Player, ShopQueue
from ..struct.item import ItemDict
from ..util import (
    create_header,
    set_player_items,
    set_player_stats
)

def show_shop(player: Player, item_dict: ItemDict):
    """Main handler of shop feature. Player can
    select all of available items and add to cart.
    """
    shop_queue = ShopQueue()
    while True:
        header_len = create_header(player.name, player.money, "SHOP")
        print("Here you can purchase items.")
        print("Select an item to add to your")
        print("cart.\n")
        item_codes: dict[str, str] = {}
        for i, item in enumerate(item_dict.values(), 1):
            item_codes[str(i)] = item.code
            print(f"{f'[{i}]':<4} {item.name:<14} ({item.price:<3} Coin)")
        print("=" * header_len)
        print("[0] View Cart")
        print("[*] Back")
        choice = input("Your Choice: ")
        match choice:
            case "0":
                _view_cart(player, shop_queue)
            case _:
                try:
                    selected_item = item_dict[item_codes[choice]]
                    print("\n" + shop_queue.enqueue(selected_item))
                    input("[OK]")
                except KeyError:
                    break


# PRIVATE FUNCTION
def _pay(player: Player, queue: ShopQueue):
    """Pay handler, will return when player's
    money not enough to pay an item, all remain
    items in cart will reset."""
    header_len = create_header(player.name, player.money, "SHOP")

    if queue.is_empty():
        print("Nothing to pay")
        print("=" * header_len)
        input("[OK]")
        return

    while True:
        item = queue.dequeue()
        if item is None:
            break
        if item.price > player.money:
            print(f"Not enough money to buy {item.name}.")
            break

        player.inventory.insert(item, 1)
        player.money -= item.price
        set_player_items(player.name, player.get_items())
        set_player_stats(player.name, player.get_stats())
        print(f"Buying {item.name:<14} -{item.price}")
    print("=" * header_len)
    input("[OK]")


def _view_cart(player: Player, queue: ShopQueue):
    """View all items on cart."""
    header_len = create_header(player.name, player.money, "SHOP")
    if queue.is_empty():
        print("Your cart is empty.")
        print("=" * header_len)
        input("[Back]")
        return

    for item in queue.list:
        print(f"{item.name:<14} ({item.price:<3} Coin)")
    print("=" * header_len)
    print("[0] Pay")
    print("[*] Back")
    choice = input("Your Choice: ")
    match choice:
        case "0":
            _pay(player, queue)
        case _:
            pass
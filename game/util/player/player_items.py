from ...inventory import Inventory, Item

def get_player_items(username: str, items: dict[str, Item]) -> Inventory:
    inventory = Inventory()

    with open(f"game/storage/items/{username}", "r") as f:
        for line in f:
            code, qty = line.split(",", 1)
            inventory.insert(items[code], int(qty))
    
    return inventory

def set_player_items():
    pass
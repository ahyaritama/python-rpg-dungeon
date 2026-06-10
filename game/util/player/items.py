def get_player_items(username: str) -> list[tuple[str, int]]:
    item_list: list[tuple[str, int]] = []
    with open(f"game/storage/items/{username}", "r") as f:
        for line in f:
            line_strip = line.strip()
            if line_strip == "":
                continue

            raw_code, raw_qty = line_strip.split(",", 1)
            code = raw_code.strip()
            qty = int(raw_qty)
            item_list.append((code, qty))
    
    return item_list

def set_player_items(username: str, item_list: list[tuple[str, int]]):
    with open(f"game/storage/items/{username}", "w") as f:
        for code, qty in item_list:
            f.write(f"{code},{qty}\n")
            

# def get_player_items(username: str, items: dict[str, Item]) -> Inventory:
#     inventory = Inventory()

#     with open(f"game/storage/items/{username}", "r") as f:
#         for line in f:
#             code, qty = line.split(",", 1)
#             inventory.insert(items[code], int(qty))
    
#     return inventory

# def set_player_items(username: str, bag: Inventory):
#     with open(f"game/storage/items/{username}", "w") as f:
#         current = bag.head
#         while current:
#             f.write(f"{current.data.code},{current.qty}\n")
#             current = current.next
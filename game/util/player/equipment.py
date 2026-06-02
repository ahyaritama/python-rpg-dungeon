from ...inventory import Equipment, Item

def get_player_equipment(username: str, items: dict[str, Item]) -> Equipment:
    codes: set[str] = set()
    itemset: set[Item] = set()
    with open(f"game/storage/equipment/{username}", "r") as f:
        for line in f:
            codes.add(str(line).strip())
            itemset.add(items[str(line).strip()])

    return Equipment(codes, itemset)

def set_player_equipment(username: str, codes: set[str]):
    with open(f"game/storage/equipment/{username}", "w") as f:
        for code in codes:
            f.write(code + "\n")
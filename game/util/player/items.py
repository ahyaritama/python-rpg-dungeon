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
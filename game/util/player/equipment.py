def get_player_equipment(username: str) -> set[str]:
    code_set: set[str] = set()
    with open(f"game/storage/equipment/{username}", "r") as f:
        for line in f:
            code = line.strip()
            if code == "":
                continue
            code_set.add(code)
    
    return code_set

def set_player_equipment(username: str, code_set: set[str]):
    with open(f"game/storage/equipment/{username}", "w") as f:
        for code in code_set:
            f.write(code + "\n")
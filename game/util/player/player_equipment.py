def get_player_equipment(username: str):
    stats: dict[str, int] = {}
    with open(f"game/storage/equipment/{username}", "r") as f:
        for line in f:
            code = str(line).strip()
            
    
    return stats

def set_player_equipment():
    pass
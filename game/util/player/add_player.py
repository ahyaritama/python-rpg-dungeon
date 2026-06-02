from ...const import DEFAULT_STATS

def add_player(username: str, password: str) -> dict[str, int]:
    with open("game/storage/auth", "a") as f:
        f.write(f"{username},{password}\n")
    
    with open(f"game/storage/equipment/{username}", "x") as f:
        pass

    with open(f"game/storage/items/{username}", "x") as f:
        pass

    with open(f"game/storage/skills/{username}", "x") as f:
        pass

    with open(f"game/storage/stats/{username}", "w") as f:
        for k, v in DEFAULT_STATS.items():
            f.write(f"{k}={v}\n")
    
    return DEFAULT_STATS
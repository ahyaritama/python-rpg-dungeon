from .stats import get_player_stats
from .rooms import get_player_rooms

from ...const import DEFAULT_STATS, DEFAULT_POSITION

def add_player(username: str, password: str):
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
    
    with open(f"game/storage/rooms/{username}", "w") as f:
        f.write("Main Gate\n\n\n")
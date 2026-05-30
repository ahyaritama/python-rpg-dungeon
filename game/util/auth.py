from ..const import DEFAULT_STATS
from ..struct.player import Player


def add_player(username: str, password: str) -> dict[str, int]:
    with open("game/storage/auth", "a") as f:
        f.write(f"{username},{password}\n")
    
    with open(f"game/storage/items/{username}", "x") as f:
        pass

    with open(f"game/storage/skills/{username}", "x") as f:
        pass

    with open(f"game/storage/stats/{username}", "w") as f:
        for k, v in DEFAULT_STATS.items():
            f.write(f"{k}={v}\n")

    return DEFAULT_STATS


def get_player_items(username: str):
    pass


def get_player_skills(username: str):
    pass


def get_player_stats(username: str) -> dict[str, int]:
    stats: dict[str, int] = {}
    with open(f"game/storage/stats/{username}", "r") as f:
        for line in f:
            key, value = line.split("=", 1)
            stats[key] = int(value)
    
    return stats


def validate(username: str, password: str) -> bool:
    username_status = True
    password_status = True
    message = ""

    if len(username) == 0:
        username_status = False
        message += "[*] Username cannot be empty"
    elif not all(x.isalnum() or x in {"-", "_"} for x in username):
        username_status = False
        message += "[*] Username can only contain alphanumeric, - and _\n"

    if len(password) < 8:
        password_status = False
        message += "[*] Minimum password length is 8 characters\n"
        
    return username_status and password_status, message
from core.const import DEFAULT_STATS
from structure import Player

def add_player(username: str, password: str):
    with open("storage/auth", "a") as f:
        f.write(f"{username},{password}\n")
    
    with open(f"storage/stats/{username}", "w") as f:
        for k, v in DEFAULT_STATS.items():
            f.write(f"{k}={v}\n")
    
    return DEFAULT_STATS

def get_player(username: str):
    stats = {}
    with open(f"storage/stats/{username}", "r") as f:
        for l in f:
            key, value = l.split("=", 1)
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
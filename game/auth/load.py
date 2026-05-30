def load() -> dict[str, str]:
    try:
        f = open("game/storage/auth")
    except FileNotFoundError:
        open("game/storage/auth", "x")
        return {}
    
    auth_dict: dict[str, str] = {}
    for l in f:
        username, password = l.split(",", 2)
        auth_dict[username] = str(password).strip()
    
    f.close()
    return auth_dict
def load():
    try:
        f = open("storage/auth")
    except FileNotFoundError:
        open("storage/auth", "x")
        return {}
    
    auth_dict = {}
    for l in f:
        username, password = l.split(",", 2)
        auth_dict[username] = str(password).strip()
    
    f.close()
    return auth_dict
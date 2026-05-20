def load():
    try:
        f = open("storage/auth")
    except FileNotFoundError:
        f = open("storage/auth", "w")
    
    auth_dict = {}
    for l in f:
        username, password = l.split(",", 2)
        auth_dict[username] = password

    f.close()
    return auth_dict
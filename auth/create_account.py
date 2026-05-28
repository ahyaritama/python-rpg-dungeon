from structure import Player
from utils import add_player, validate

def create_account(x):
    while True:
        username = input("Input your username: ")
        if username in x:
            print("[*] Username already taken\n")
            continue
        
        password = input("Input your password: ")
        ok, msg = validate(username, password)
        if ok:
            x[username] = password
            break
        print(msg)

    stats = add_player(username, password)
    print(stats)
    return Player(username, **stats)
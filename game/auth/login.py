from ..inventory.item import Item
from ..struct.player import Player
from ..util.auth import (
    get_player_items,
    get_player_skills,
    get_player_stats
)

def login(players: dict[str, str], items: dict[str, Item]):
    username = input("Input your username: ")
    password = input("Input your password: ")

    if (
        not username in players
        or players[username] != password
    ):
        print("Invalid username or password submited\n")
        return

    p_items = get_player_items(username, items)
    skills = get_player_skills(username)
    stats = get_player_stats(username)

    print(f"Successfully login using account {username}\n")
    return Player(username, stats, skills, p_items)
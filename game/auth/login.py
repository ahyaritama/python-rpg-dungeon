from ..inventory import Item
from ..struct import Player
from ..util import (
    get_player_equipment,
    get_player_items,
    get_player_rooms,
    get_player_skills,
    get_player_stats
)

def login(players: dict[str, str], items: dict[str, Item]):
    print("\n(Use CTRL + C to quit)")
    while True:
        try:
            username = input("Input your username: ")
            password = input("Input your password: ")

            if (username in players and players[username] == password):
                break
            
            print("Invalid username or password submited\n")
        except KeyboardInterrupt:
            return

    equipment = get_player_equipment(username, items)
    p_items = get_player_items(username, items)
    rooms = get_player_rooms(username)
    skills = get_player_skills(username)
    stats = get_player_stats(username)

    print(f"Successfully login using account {username}\n")
    return Player(username, stats, skills, p_items, equipment, rooms)
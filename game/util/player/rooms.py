def get_player_rooms(username: str) -> list[str, set[str]]:
    raw_rooms: list[str] = []
    with open(f"game/storage/rooms/{username}", "r") as f:
        for line in f:
            raw_rooms.append(str(line).strip())
    
    position, *visited_room = raw_rooms
    return [position, set(visited_room)]

def set_player_rooms(username: str, position: str, visited_room: set[str]):
    with open(f"game/storage/rooms/{username}", "w") as f:
        f.write(position + "\n")
        for room in visited_room:
            f.write(room + "\n")
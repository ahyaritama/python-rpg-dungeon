def get_player_rooms(username: str) -> list[str, list[str], set[str]]:
    raw_rooms: list[str] = []
    with open(f"game/storage/rooms/{username}", "r") as f:
        for line in f:
            raw_rooms.append(str(line).strip())
    
    position, raw_move, *visited_room = raw_rooms
    move = str(raw_move).split(",") if str(raw_move) != "" else []
    return [position, move, set(visited_room)]

def set_player_rooms(username: str, position: str, move: list[str], visited_room: set[str]):
    with open(f"game/storage/rooms/{username}", "w") as f:
        f.write(position + "\n")
        f.write(",".join(move) + "\n")
        for room in visited_room:
            f.write(room + "\n")
def get_player_rooms(username: str) -> tuple[str, list[str], set[str]]:
    raw_rooms: list[str] = []
    with open(f"game/storage/rooms/{username}", "r") as f:
        for line in f:
            raw_rooms.append(line.strip())
    
    position, raw_moves, raw_cleared_rooms = raw_rooms
    move_list = raw_moves.split(",") if raw_moves != "" else []
    cleared_rooms = set(raw_cleared_rooms.split(",")) if raw_cleared_rooms != "" else set()

    return position, move_list, cleared_rooms

def set_player_rooms(username: str, rooms: tuple[str, list[str], set[str]]):
    position, moves, cleared_rooms = rooms
    with open(f"game/storage/rooms/{username}", "w") as f:
        f.write(f"{position}\n")
        f.write(f"{','.join(moves)}\n")
        f.write(f"{','.join(list(cleared_rooms))}\n")



#  def get_player_rooms(username: str) -> list[str, list[str], set[str]]:
#     raw_rooms: list[str] = []
#     with open(f"game/storage/rooms/{username}", "r") as f:
#         for line in f:
#             raw_rooms.append(str(line).strip())
    
#     position, raw_move, *visited_room = raw_rooms
#     move = str(raw_move).split(",") if str(raw_move) != "" else []
#     return [position, move, set(visited_room)]

# def set_player_rooms(username: str, position: str, move: list[str], visited_room: set[str]):
#     with open(f"game/storage/rooms/{username}", "w") as f:
#         f.write(position + "\n")
#         f.write(",".join(move) + "\n")
#         for room in visited_room:
#             f.write(room + "\n")
from .item import ItemDict, ItemList
from .monster import Monster

class MoveStack:
    """Stack implementation to undo a move."""
    def __init__(self, stack: list[str]):
        self.stack = []

    def push(self, room_name: str):
        self.stack.append(room_name)

    def pop(self) -> str | None:
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self) -> bool:
        return len(self.stack) == 0

class Room:
    def __init__(self, name: str, monster: Monster, item_list: ItemList):
        self.name = name
        self.monster = monster
        self.item_list = item_list

class Map:
    """Graph implementation as a dungeon map."""
    def __init__(self):
        self.graph: dict[str, tuple[Room, list[Room]]] = {}
    
    def add_room(self, room: Room):
        if room.name not in self.graph:
            self.graph[room.name] = (room, [])

    def connect_room(self, x: Room, y: list[Room]):
        self.add_room(x)
        self.graph[x.name][1].extend(y)
    
    def display_room(self):
        for k, v in self.graph.items():
            connected_room = ", ".join(room.name for room in v[1])
            print(f"- {k} connected to:", connected_room)


def init(monster: list[Monster], item_dict: ItemDict):
    """Initialize and return a full dungeon map."""
    main_gate = Room("Main Gate", monster[0], [])
    west_hallway = Room("West Hallway", monster[1], [item_dict["DEF_02"]])
    central_hall = Room("Central Hall", monster[2], [item_dict["HP_02"]])
    east_hallway = Room("East Hallway", monster[3], [item_dict["HP_03"], item_dict["ATK_02"]])
    armory = Room("Armory", monster[4], [item_dict["DEF_02"], item_dict["ATK_02"], item_dict["HP_01"]])
    guard_room = Room("Guard Room", monster[5],[item_dict["ATK_01"], item_dict["HP_02"]])
    library = Room("Library", monster[6], [item_dict["HP_01"], item_dict["DEF_03"]])
    laboratory = Room("Laboratory", monster[7], [item_dict["HP_02"]])
    basement = Room("Basement", monster[8], [])
    trap_room = Room("Trap Room", monster[9], [])
    throne_room = Room("Throne Room", monster[10], [item_dict["HP_02"], item_dict["ATK_01"], item_dict["DEF_02"]])
    treasure_room = Room("Treasure Room", monster[11], [item_dict["HP_02"], item_dict["ATK_03"], item_dict["DEF_01"]])

    dungeon_map = Map()
    dungeon_map.connect_room(main_gate, [west_hallway, central_hall, east_hallway])
    dungeon_map.connect_room(west_hallway, [main_gate, armory])
    dungeon_map.connect_room(central_hall, [main_gate, guard_room, library, laboratory])
    dungeon_map.connect_room(east_hallway, [main_gate, basement])
    dungeon_map.connect_room(armory, [west_hallway, guard_room, throne_room])
    dungeon_map.connect_room(guard_room, [central_hall, armory])
    dungeon_map.connect_room(library, [central_hall, throne_room])
    dungeon_map.connect_room(laboratory, [central_hall, trap_room])
    dungeon_map.connect_room(basement, [east_hallway, trap_room])
    dungeon_map.connect_room(trap_room, [laboratory, basement])
    dungeon_map.connect_room(throne_room, [armory, library, treasure_room])
    dungeon_map.connect_room(treasure_room, [throne_room])

    return dungeon_map
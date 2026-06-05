from .monster import Monster

from ..inventory import Item

class Room:
    def __init__(self, name: str, monster: Monster, items: list[Item]):
        self.name = name
        self.monster = monster
        self.items = items

class Map:
    def __init__(self):
        self.graph: dict[str, list[Room, list[Room]]] = {}
    
    def add_room(self, room: Room):
        if room.name not in self.graph:
            self.graph[room.name] = [room]

    def connect_room(self, x: Room, y: list[Room]):
        self.add_room(x)
        self.graph[x.name].append(y)
    
    def display_room(self):
        for k, v in self.graph.items():
            connected_room = ", ".join(room.name for room in v[1])
            print(f"- {k} connected to:", connected_room)




def init(monster: list[Monster], items: dict[str, Item]):
    main_gate = Room("Main Gate", monster[0], [])
    west_hallway = Room("West Hallway", monster[1], [items["DEF_02"]])
    central_hall = Room("Central Hall", monster[2], [items["HP_02"]])
    east_hallway = Room("East Hallway", monster[3], [items["HP_03"], items["ATK_02"]])
    armory = Room("Armory", monster[4], [items["DEF_02"], items["ATK_02"], items["HP_01"]])
    guard_room = Room("Guard Room", monster[5],[items["ATK_01"], items["HP_02"]])
    library = Room("Library", monster[6], [items["HP_01"], items["DEF_03"]])
    laboratory = Room("Laboratory", monster[7], [items["HP_02"]])
    basement = Room("Basement", monster[8], [])
    trap_room = Room("Trap Room", monster[9], [])
    throne_room = Room("Throne Room", monster[10], [items["HP_02"], items["ATK_01"], items["DEF_02"]])
    treasure_room = Room("Treasure Room", monster[11], [items["HP_02"], items["ATK_03"], items["DEF_01"]])

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
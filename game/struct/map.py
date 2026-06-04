from .monster import Monster

from ..inventory import Item

class Room:
    def __init__(self, name: str, monster: Monster, items: list[Item]):
        self.name = name
        self.monster = monster
        self.items = items

class Map:
    def __init__(self, start: Room):
        self.start = start
        self.graph: dict[str, list[Room]] = {
            start.name: []
        }
    
    def add_room(self, room_name: str):
        if room_name not in self.graph:
            self.graph[room_name] = []

    def connect_room(self, x: Room, y: list[Room]):
        self.add_room(x.name)
        self.graph[x.name].extend(y)
    
    def display_room(self):
        for k, v in self.graph.items():
            connected_room = ", ".join(room.name for room in v)
            print(f"- {k} connected to:", connected_room)




def init(monster: list[Monster], items: dict[str, Item]):
    main_gate = Room("Main Gate", monster[0], [items["HP_01"]])
    west_hallway = Room("West Hallway", monster[1], [items["HP_01"]])
    central_hall = Room("Central Hall", monster[2], [items["HP_01"]])
    east_hallway = Room("East Hallway", monster[3], [items["HP_01"]])
    armory = Room("Armory", monster[4], [items["HP_01"]])
    guard_room = Room("Guard Room", monster[5], [items["HP_01"]])
    library = Room("Library", monster[6], [items["HP_01"]])
    laboratory = Room("Laboratory", monster[7], [items["HP_01"]])
    basement = Room("Basement", monster[8], [items["HP_01"]])
    trap_room = Room("Trap Room", monster[9], [items["HP_01"]])
    throne_room = Room("Throne Room", monster[10], [items["HP_01"]])
    treasure_room = Room("Treasure Room", monster[11], [items["HP_01"]])

    dungeon_map = Map(main_gate)
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
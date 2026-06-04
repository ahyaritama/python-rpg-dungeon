from .character import Character

from ..inventory import (
    Equipment,
    Inventory,
    Item
)

class Player(Character):
    def __init__(
        self,
        name: str,
        stats: dict[str, int],
        skills: set[str],
        bag: Inventory,
        equipment: Equipment,
        room: list[str, set[str]]
    ):
        self.money, *stats, self.exp, self.level = stats.values()
        self.skills = skills
        self.bag = bag
        self.equipment = equipment
        self.position = room[0]
        self.visited_room = room[1]

        super().__init__(name, *stats)
    
    def equip(self, item: Item):
        return self.equipment.equip(self.name, item)  

    def learn_skill(self):
        pass

    def is_room_visited(self, room_name: str) -> bool:
        return room_name in self.__visited_room

    def visit_room(self, room_name: str) -> bool:
        if self.is_room_visited(room_name):
            return False
        
        self.visited_room.add(room_name)
        return True
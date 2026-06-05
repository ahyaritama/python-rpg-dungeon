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
        self.cleared = room[1]

        super().__init__(name, *stats)

    def is_alive(self):
        return self.stats["HP"] > 0

    def check_level_up(self):
        if self.exp > 100:
            self.exp -= 100
            self.level += 1
            self.stats["Max HP"] += 20
            self.stats["ATK"] += 3
            self.stats["DEF"] += 2


    def equip(self, item: Item):
        return self.equipment.equip(self.name, item)  

    def learn_skill(self):
        pass

    def is_room_cleared(self, room_name: str) -> bool:
        return room_name in self.cleared

    def clear_room(self, room_name: str) -> bool:
        if self.is_room_cleared(room_name):
            return False
        
        self.cleared.add(room_name)
        return True

    def reset(self):
        from ..util import (
            set_player_equipment,
            set_player_items,
            set_player_rooms,
            set_player_skills,
            set_player_stats
        )

        self.money = 0
        self.exp = 0
        self.level = 1
        self.skills = set()
        self.bag = Inventory()
        self.equipment = Equipment(set(), set())
        self.position = "Main Gate"
        self.cleared = set()
        self.skill = set()
        self.stats = {
            "HP": 0,
            "Max HP": 100,
            "ATK": 15,
            "DEF": 5,
        }

        set_player_equipment(self.name, set())
        set_player_items(self.name, self.bag)
        set_player_rooms(self.name, self.position, self.cleared)
        set_player_skills(self.name, set())
        set_player_stats(self)

    def set_position(self, room_name: str):
        self.position = room_name
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
        equipment: Equipment
    ):
        self.money, *stats = stats.values()
        self.skills = skills
        self.bag = bag
        self.equipment = equipment

        super().__init__(name, *stats)
    
    def equip(self, item: Item):
        return self.equipment.equip(self.name, item)  

    def learn_skill(self):
        pass
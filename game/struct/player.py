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
        skills,
        bag: Inventory,
        equipment: Equipment
    ):
        self.money, *stats = stats.values()
        self.skills = skills
        self.bag = bag
        self.equipment = equipment

        super().__init__(name, *stats)
    
    def learn_skill(self):
        pass

    def equip(self, item: Item):
        pass
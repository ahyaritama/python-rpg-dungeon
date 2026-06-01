from .character import Character

from ..inventory import Inventory

class Player(Character):
    def __init__(
        self,
        name: str,
        stats: dict[str, int],
        skills,
        bag: Inventory
    ):
        self.money, *stats = stats.values()
        self.skills = skills
        self.bag = bag

        super().__init__(name, *stats)
    
    def learn_skill(self):
        pass
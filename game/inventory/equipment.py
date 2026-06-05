from .item import Item

class Equipment:
    def __init__(self, codes: set[str], items: set[Item]):
        self.equipped = codes
        self.equipment = items
    
    def equip(self, username: str, item: Item) -> tuple[bool, str]:
        if item.code in self.equipped:
            return False, "You have been equipped with this item\n"
        elif "HP" in item.code:
            return False, "HP item cannot equipped\n"

        self.equipped.add(item.code)
        self.equipment.add(item)

        from ..util import set_player_equipment
        set_player_equipment(username, self.equipped)
        return True, f"{item.name} item successfully equipped"
    
    def get_total_attack(self) -> int:
        total = 0
        for item in self.equipment:
            if "ATK" in item.code:
                total += item.effect
        return total
    
    def get_total_defence(self) -> int:
        total = 0
        for item in self.equipment:
            if "DEF" in item.code:
                total += item.effect
        return total
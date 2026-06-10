from .item import Item, ItemSet

from ..util import set_player_equipment

class Equipment:
    def __init__(self, code_set: set[str], item_set: ItemSet):
        self.code_set = code_set
        self.item_set = item_set
    
    def equip(self, username: str, item: Item) -> tuple[bool | None, str]:
        if item.code in self.code_set:
            return False, "You have been equipped with this item"
        elif "HP" in item.code:
            return None, ""

        self.code_set.add(item.code)
        self.item_set.add(item)
        set_player_equipment(username, self.code_set)

        return True, f"{item.name} successfully equipped"

    def get_total_attack(self) -> int:
        total = 0
        for item in self.item_set:
            if "ATK" in item.code:
                total += item.effect
        return total
    
    def get_total_defence(self) -> int:
        total = 0
        for item in self.item_set:
            if "DEF" in item.code:
                total += item.effect
        return total

# class Equipment:
#     def __init__(self, codes: set[str], items: ItemSet):
#         self.equipped = codes
#         self.equipment = items
    
#     def equip(self, username: str, item: Item) -> tuple[bool, str]:
#         if item.code in self.equipped:
#             return False, "You have been equipped with this item\n"
#         elif "HP" in item.code:
#             return None, ""

#         self.equipped.add(item.code)
#         self.equipment.add(item)

#         from ..util import set_player_equipment
#         set_player_equipment(username, self.equipped)
#         return True, f"{item.name} item successfully equipped"
    
#     def get_total_attack(self) -> int:
#         total = 0
#         for item in self.equipment:
#             if "ATK" in item.code:
#                 total += item.effect
#         return total
    
#     def get_total_defence(self) -> int:
#         total = 0
#         for item in self.equipment:
#             if "DEF" in item.code:
#                 total += item.effect
#         return total
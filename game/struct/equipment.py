from .item import Item, ItemSet

from ..util import set_player_equipment

class Equipment:
    """Save all player ATK and DEF items used."""
    def __init__(self, code_set: set[str], item_set: ItemSet):
        self.code_set = code_set
        self.item_set = item_set
    
    def equip(self, username: str, item: Item) -> tuple[bool | None, str]:
        """Use ATK or DEF items if not used yet,
        return None if HP item equipped.
        """
        if item.code in self.code_set:
            return False, "You have been equipped with this item"
        elif "HP" in item.code:
            return None, ""

        self.code_set.add(item.code)
        self.item_set.add(item)
        set_player_equipment(username, self.code_set)

        return True, f"{item.name} successfully equipped"

    def get_total_attack(self) -> int:
        """Return bonus ATK attribute from ATK items."""
        total = 0
        for item in self.item_set:
            if "ATK" in item.code:
                total += item.effect
        return total
    
    def get_total_defence(self) -> int:
        """Return bonus DEF attribute from DEF items."""
        total = 0
        for item in self.item_set:
            if "DEF" in item.code:
                total += item.effect
        return total
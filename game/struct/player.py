from .character import Character
from .equipment import Equipment
from .inventory import Inventory
from .item import Item
from .map import MoveStack

from ..util import (
    set_player_equipment,
    set_player_items,
    set_player_rooms,
    set_player_skills,
    set_player_stats
)

type PlayerDict = dict[str, str]

class Player(Character):
    def __init__(
            self,
            name: str,
            stats_dict: dict[str, int],
            inventory: Inventory,
            equipment: Equipment,
            skill_set: set[str],
            rooms_tup: tuple[str, list[str], set[str]]
    ):
        super().__init__(
            name,
            stats_dict.get("hp", 100),
            stats_dict.get("max_hp", 100),
            stats_dict.get("attack", 15),
            stats_dict.get("defence", 5),
        )

        self.money = stats_dict.get("money", 0)
        self.exp = stats_dict.get("exp", 0)
        self.level = stats_dict.get("level", 1)

        self.inventory = inventory
        self.equipment = equipment
        self.skill_set = skill_set
        self.position = rooms_tup[0]
        self.move_list = MoveStack(rooms_tup[1])
        self.cleared_rooms = rooms_tup[2]

    def check_level_up(self):
        """Check if player can up level (exp >= 100) and
        update base stats."""
        if self.exp < 100:
            return
        
        print("\nYour level has increased!")
        print(f"Level  : {self.level} -> {self.level + 1}")
        print(f"Max HP : {self.stats["Max HP"]} -> {self.stats["Max HP"] + 20}")
        print(f"ATK    : {self.stats["ATK"]} -> {self.stats["ATK"] + 3}")
        print(f"DEF    : {self.stats["DEF"]} -> {self.stats["DEF"] + 2}")

        self.exp -= 100
        self.level += 1
        self.stats["Max HP"] += 20
        self.stats["HP"] = self.stats["Max HP"]
        self.stats["ATK"] += 3
        self.stats["DEF"] += 2

        self.check_level_up()
    
    def clear_room(self, room_name: str) -> bool:
        """Mark a room as visited."""
        if self.is_room_cleared(room_name):
            return False
        
        self.cleared_rooms.add(room_name)
        return True
    
    def equip(self, item: Item) -> tuple[bool, str]:
        """Equip an item if ATK or DEF item, consume if HP item."""
        ok, msg = self.equipment.equip(self.name, item)
        if ok is None:
            self.stats["HP"] += item.effect
            if self.stats["HP"] > self.stats["Max HP"]:
                self.stats["HP"] = self.stats["Max HP"]
            msg = f"{item.name} successfully consume (HP +{item.effect})"
            ok = True

        return ok, msg

    def get_items(self) -> list[tuple[str, int]]:
        """Get player's items as raw list."""
        item_list: list[tuple[str, int]] = []

        current = self.inventory.head
        while current:
            item_list.append((current.data.code, current.qty))
            current = current.next
        
        return item_list
    
    def get_rooms(self) -> tuple[str, list[str], set[str]]:
        """Get player's position, moves, and visited room as raw tuple."""
        return (self.position, self.move_list.stack, self.cleared_rooms)

    def get_stats(self) -> dict[str, int]:
        """Get player's stats as raw dict."""
        return {
            "money": self.money,
            "hp": self.stats["HP"],
            "max_hp": self.stats["Max HP"],
            "attack": self.stats["ATK"],
            "defence": self.stats["DEF"],
            "exp": self.exp,
            "level": self.level
        }

    def is_alive(self):
        return self.stats["HP"] > 0

    def is_room_cleared(self, room_name: str) -> bool:
        return room_name in self.cleared_rooms
    
    def reset(self):
        """Reset all player's progress."""
        self.money = 0
        self.exp = 0
        self.level = 1

        self.inventory = Inventory()
        self.equipment = Equipment(set(), set())
        self.skill_set = set()
        self.position = "Main Gate"
        self.move_list = MoveStack(list())
        self.cleared_rooms = set()

        super().reset_stats()

        set_player_equipment(self.name, self.equipment.code_set)
        set_player_items(self.name, self.get_items())
        set_player_rooms(self.name, self.get_rooms())
        set_player_skills(self.name, self.skill_set)
        set_player_stats(self.name, self.get_stats())
    
    def set_position(self, room_name: str):
        """Set player's position"""
        self.position = room_name
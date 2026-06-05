from .monster import Monster
from .player import Player


class BattleNode:
    def __init__(self, character: Player | Monster):
        self.character = character
        self.next: BattleNode = None

class Battle:
    def __init__(self):
        self.head: BattleNode = None
        self.total_char = 0
        self.cooldown: int = 0
    
    def add_character(self, character: Player | Monster):
        new_node = BattleNode(character)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = current
        
        self.total_char += 1

    def remove_character(self, character: Player | Monster):
        if not self.head:
            return
        
        current = self.head
        prev: BattleNode = None

        while True:
            if current.character == character:
                break
            prev = current
            current = current.next
            if current == self.head:
                return
        
        if current == self.head and current.next == self.head:
            self.head = None
        else:
            if current == self.head:
                x = self.head
                while x.next != self.head:
                    x = x.next
                self.head = self.head.next
                x.next = self.head
            else:
                prev.next = current.next
        
        self.total_char -= 1
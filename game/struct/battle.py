from .monster import Monster
from .player import Player

class BattleNode:
    """Circular Linked List Node for battle implementation
    with character as data.
    """
    def __init__(self, char: Player | Monster):
        self.char = char
        self.next: BattleNode | None = None
    
class Battle:
    """Circular Linked List implementation for battle."""
    def __init__(self):
        self.head: BattleNode | None = None
        self.total_char = 0
        self.cooldown = 0
    
    def add_char(self, char: Player | Monster):
        """Add character node and add total character by 1."""
        new_node = BattleNode(char)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next and current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.total_char += 1

    def remove_char(self, char: Player | Monster):
        """Remove character node and substract total character by 1."""
        if not self.head:
            return

        current = self.head.next
        prev: BattleNode = self.head
        while current:
            if current.char == char:
                break
            prev = current
            current = current.next
            if current == self.head.next:
                return
        
        if current:
            if current is self.head and current.next is self.head:
                self.head = None
            else:
                prev.next = current.next
        self.total_char -= 1
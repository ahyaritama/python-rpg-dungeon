from .item import Item

class InventoryNode:
    """Double Linked List Node for inventory implementation
    with item as data.
    """
    def __init__(self, data: Item, qty: int):
        self.data = data
        self.qty = qty
        self.prev: InventoryNode | None = None
        self.next: InventoryNode | None = None

class Inventory:
    """Double Linked List implementation for inventory."""
    def __init__(self):
        self.head: InventoryNode | None = None

    def search_by_name(self, name: str) -> InventoryNode | None:
        """Linear Search for search item by name"""
        current = self.head
        while current is not None:
            if current.data.name == name:
                return current
            current = current.next

        return None
    
    def search_by_code(self, code: str) -> InventoryNode | None:
        """Linear Search for search item by name"""
        current = self.head
        
        while current is not None:
            if current.data.code == code:
                return current
            current = current.next
            
        return None

    def insert(self, data: Item, qty: int):
        """Insert an item node to inventory's Double Linked List."""
        if self.head is None:
            self.head = InventoryNode(data, qty)
            return
        
        current = tail = self.head
        while current is not None:
            if current.data.name == data.name:
                current.qty += qty
                return
            elif current.next is None:
                tail = current
            current = current.next
        
        new_item = InventoryNode(data, qty)
        tail.next = new_item
        new_item.prev = tail

    def delete(self, data: Item):
        """Delete an item node from inventory's Double Linked List."""
        current = self.head

        while current is not None:
            if current.data.name == data.name:
                if current == self.head:    
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None

                else:
                    if current.prev is not None:
                        current.prev.next = current.next
                        if current.next is not None:
                            current.next.prev = current.prev
                
                return True
            
            current = current.next

        return False
    
    def sort_by_code(self, ascending: bool = True):
        """Sorting implementation for sort item by code"""
        if self.head is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if ascending:
                    condition = current.data.code > current.next.data.code
                else:
                    condition = current.data.code < current.next.data.code

                if condition:
                    current.data, current.next.data = current.next.data, current.data
                    current.qty, current.next.qty = current.next.qty, current.qty
                    swapped = True
                
                current = current.next

    def sort_by_name(self, ascending: bool = True):
        """Sorting implementation for sort item by name"""
        if self.head is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if ascending:
                    condition = current.data.name > current.next.data.name
                else:
                    condition = current.data.name < current.next.data.name

                if condition:
                    current.data, current.next.data = current.next.data, current.data
                    current.qty, current.next.qty = current.next.qty, current.qty
                    swapped = True
                
                current = current.next

    def sort_by_price(self, ascending: bool = True):
        """Sorting implementation for sort item by price"""
        if self.head is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if ascending:
                    condition = current.data.price > current.next.data.price
                else:
                    condition = current.data.price < current.next.data.price

                if condition:
                    current.data, current.next.data = current.next.data, current.data
                    current.qty, current.next.qty = current.next.qty, current.qty
                    swapped = True
                
                current = current.next
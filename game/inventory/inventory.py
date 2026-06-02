from .item import Item

class InventoryItem:
    def __init__(self, data: Item, qty: int):
        self.data = data
        self.qty = qty
        self.prev = None
        self.next = None

class Inventory:
    def __init__(self):
        self.head: InventoryItem = None

    def search_by_name(self, name) -> tuple[Item, int]:
        current = self.head

        while current is not None:
            if current.data.name == name:
                return current.data, current.qty
            current = current.next

        return None, 0
    
    def insert(self, data: Item, qty: int):
        if self.head is None:
            self.head = InventoryItem(data, qty)
            return 
        
        current = self.head
        tail: InventoryItem = None
        while current is not None:
            if current.data.name == data.name:
                current.qty += qty
                return
            elif current.next is None:
                tail = current
            current = current.next
        
        new_item = InventoryItem(data, qty)
        tail.next = new_item
        new_item.prev = tail

    def delete(self, data : Item):
        current = self.head

        while current is not None:
            if current.data.name == data.name:
                if current == self.head:    
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                
                else:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev
                
                return True
            
            current = current.next

        return False
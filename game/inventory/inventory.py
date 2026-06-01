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
        while current is not None:
            if current.data.name == data.name:
                current.qty += qty
                return
            current = current.next
        
        new_item = InventoryItem(data, qty)
        
        new_item.next = self.head
        self.head.prev = new_item
        self.head = new_item

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
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
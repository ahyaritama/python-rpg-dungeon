from .item import Item

class InventoryItem:
    def __init__(self, data: Item):
        self.data = data
        self.prev = None
        self.next = None

class Inventory:
    def __init__(self):
        self.head: InventoryItem = None

    def search_by_name(self, name) -> Item:
        current = self.head

        while current is not None:
            if current.data.name == name:
                return current.data
            current = current.next

        return None
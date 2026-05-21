class InventoryItem:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None

    def search_by_name(self, name):
        current = self.head

        while current is not None:
            if current.data == name:
                return True
            current = current.next

        return False
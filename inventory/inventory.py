class Item:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None
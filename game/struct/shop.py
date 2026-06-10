from .item import Item, ItemList

class ShopQueue:
    def __init__(self):
        self.list: ItemList = []
    
    def enqueue(self, item) -> str:
        self.list.append(item)
        return f"{item.name} added to cart"

    def dequeue(self) -> Item | None:
        if self.is_empty():
            return None
        return self.list.pop(0)

    def is_empty(self) -> bool:
        return len(self.list) == 0
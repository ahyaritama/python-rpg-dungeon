class ShopStack:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item) -> str:
        self.queue.append(item)
        return f"{item.name} added to cart"

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
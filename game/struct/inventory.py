from .item import Item

from ..util import (
    bubble_sort_ascending,
    bubble_sort_descending
)

class InventoryNode:
    def __init__(self, data: Item, qty: int):
        self.data = data
        self.qty = qty
        self.prev: InventoryNode | None = None
        self.next: InventoryNode | None = None

class Inventory:
    def __init__(self):
        self.head: InventoryNode | None = None

    def search_by_name(self, name: str) -> InventoryNode | None:
        current = self.head
        while current is not None:
            if current.data.name == name:
                return current
            current = current.next

        return None
    
    def search_by_code(self, code: str) -> InventoryNode | None:
            current = self.head
            
            while current is not None:
                if current.data.code == code:
                    return current
                current = current.next
                
            return None

    def insert(self, data: Item, qty: int):
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

    def sort_by_code_descending(self):
        if self.head is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.data.code < current.next.data.code:
                    
                    current.data, current.next.data = current.next.data, current.data
                    current.qty, current.next.qty = current.next.qty, current.qty
                    swapped = True
                current = current.next

    def sort_by_name_descending(self):
        if self.head is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.data.name < current.next.data.name:
                    
                    current.data, current.next.data = current.next.data, current.data
                    current.qty, current.next.qty = current.next.qty, current.qty
                    swapped = True
                current = current.next

    def sort_by_price_descending(self):
        if self.head is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.data.price < current.next.data.price:
                    
                    current.data, current.next.data = current.next.data, current.data
                    current.qty, current.next.qty = current.next.qty, current.qty
                    swapped = True
                current = current.next
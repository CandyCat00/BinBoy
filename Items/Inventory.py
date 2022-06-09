from items.Objects import objects
from items.Cup import cup

class inventory():
    def __init__(self):
        self.items = list()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
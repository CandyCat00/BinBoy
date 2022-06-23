from Items import Objects
from Items import Cup

class inventory():
    def __init__(self):
        self.items = dict()

    def add_item(self, item):
        if item.name not in self.items:
            self.items[item.name] = 1
        else:
            self.items[item.name] += 1

    def remove_item(self, item_name):
        del self.items[item_name]
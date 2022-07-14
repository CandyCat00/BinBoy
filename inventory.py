
class Inventory():
    inventory = []

    def add_trash(trash):
        # adds collected trash into the array
        Inventory.inventory.append(trash)

    def display_inventory():
        # this is for the bonus level
        if (len(Inventory.inventory) > 0):
            first_item = Inventory.inventory[0]
        if (len(Inventory.inventory) > 1):
            next_item = Inventory.inventory[1]
        else:
            next_item = 'E'
        return first_item, next_item

    def delete_trash():
        #delete the first item in the array
        del Inventory.inventory[0]
        print(len(Inventory.inventory))

    def is_empty():
        if (len(Inventory.inventory) == 0):
            return True
        else:
            return False
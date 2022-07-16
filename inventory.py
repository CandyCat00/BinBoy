###############################################################################
# This class holds a list that the trash we collect gets added to throughout
# the level to be sorted later.
###############################################################################
class Inventory():
    inventory = []

    # adds collected trash into the list
    def add_trash(trash):
        Inventory.inventory.append(trash)

    # this is for the bonus level. It gets the first and second item for the
    # user to see as they are sorting them into bins
    def display_inventory():
        if (len(Inventory.inventory) > 0):
            first_item = Inventory.inventory[0]
        if (len(Inventory.inventory) > 1):
            next_item = Inventory.inventory[1]
        else:
            next_item = 'E'
        return first_item, next_item

    # This is called to the delete the trash after it has been placed in a bin
    def delete_trash():
        #delete the first item in the array
        del Inventory.inventory[0]

    # This checks if the array is empty. If it is, the bonus level ends
    def is_empty():
        if (len(Inventory.inventory) == 0):
            return True
        else:
            return False
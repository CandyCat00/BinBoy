from Items.Objects import objects

class trash(objects):
    def __init__(self):
        super().__init__(debug)
        self._x = 0
        self._y = 0
        self.image = ""
        self.name = ""

    def set_image(self, path):
        """This sets the image for the object.
        An image path should be given to the object
        to pull from."""
        self.image = path

    def set_name(self, name):
        self.name = name

    def show_trash(self,display,position):
        
        pass
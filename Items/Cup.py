from Objects import objects

class cup(objects):
    def __init__(self):
        super().__init__(debug)
        self._x = 0
        self._y = 0
        self.image = ""

    def set_image(self, path):
        """This sets the image for the object.
        An image path should be given to the object
        to pull from."""
        self.image = path
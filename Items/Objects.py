class objects():
    def __init__(self, debug=False):
        self.debug = debug

    def assign_coordinates(self,x,y):
        """This is to set the X and Y coordinates of the
        object."""
        self._x = x
        self._y = y
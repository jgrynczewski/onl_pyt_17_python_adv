class Square:
    def __init__(self, side):
        self._side = side
        self._perimeter = 4 * self._side
        self._area = self._side ** 2
        self._diagonal = self._side * (2**0.5)

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    def set_side(self, new_length):
        self.__init__(new_length)

        # lub tak
        # self._side = new_length
        # self._perimeter = 4 * new_length
        # self._area = new_length ** 2
        # self._diagonal = new_length * (2**0.5)

    def set_perimeter(self, new_length):
        new_side = new_length/4
        self.__init__(new_side)

        # self._perimeter = new_length
        # self._side = new_length/4
        # self._area  = (new_length/4)**2
        # self._diagonal = (new_length/4) * (2**0.5)

    def set_area(self, new_area):
        new_side = new_area ** 0.5
        self.__init__(new_side)

    def set_diagonal(self, new_length):
        new_side = new_length / (2**0.5)
        self.__init__(new_side)

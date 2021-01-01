from math import pi

class Circle:

    def __init__(self, radius):
        self._radius = radius
        self._area = None
        self._field = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._area = None
        self._field = None
        self._radius = value
    
    @property
    def area(self):
        if self._area is None:
            print('Calculating area')
            self._area = pi * (self.radius ** 2)
        return self._area

    @property
    def field(self):
        if self._field is None:
            print('Calculating field')
            self._field = pi * (self.radius ** 4)
        return self._field


c = Circle(4)

print(c.area)

print(c.field)
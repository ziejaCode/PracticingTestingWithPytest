class Rectangle:
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def area (self):
        return self.width * self.height 

   # def to_string(self):
      #  return 'Rectangel: width={0}, height={1}'.format(self.width, self.height)

    def __str__(self):
        return 'Rectangel: width={0}, height={1}'.format(self._width, self._height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self._width = width






r1 = Rectangle(23,67)

r1.width = -34
print(r1.width)
print(r1._width)
print(r1)
r1.set_width(56)
print(r1)
print(r1.get_width())


'''

    r1 = Rectangle(23,34)
r2 = Rectangle(23,34)
print(r1 is r2)
print(r1 == r2)
print(r1.width)
print(r1.height)
print(r1)
#print(r1.to_string())
print(str(r1))
'''
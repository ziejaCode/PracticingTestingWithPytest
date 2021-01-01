'''
This class is an example of how to use getter and 
setter in python class with backward comapatibility 
'''
class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Must be positive')
        else:
            self._width = width
         
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Must be positive')
        else:
            self._height = height

    def __str__(self):
        return 'Rectangel: width={0}, height={1}'.format(self.width, self.height)


r1 = Rectangle(45, 87)

print(r1)
# this is now how to set the value 
r1.width = 67

print(r1)




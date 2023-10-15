#!usr/bin/python3
"""
rectangle module
"""
from module.base import Base

class Rectangle(Base):
    """
    Rectangle Implementation
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init - initialization
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x position
            y: y position
            id: object id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def check(self, key, value, less_eq=True):
        """
        checks for value and type error
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        if less_eq:
            if value <= 0:
                raise ValueError("{} must be > 0".format(value))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(value))

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.check('width', width)
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.check('height', height)
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        self.check('x', x, False)
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.check('y', y, False)
        self.__y = y
    
    def area(self):
        """
        area
        """
        return self.__width * self.__height

    def display(self):
        """
        prints rectangle
        """
        for y in range(self.y):
            print()
        for i in range(self.__height):
            for x in range(self.x):
                print(' ', end='')
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        lst = (self.id, self.width, self.height, self.x, self.y)
        if args:
            self.id, self.width, self.height, self.x, self.y = \
                    args + lst[len(args):len(lst)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)


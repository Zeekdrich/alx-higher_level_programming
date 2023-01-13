#!/usr/bin/python3
"""rectangle class that inherits from base
"""

from model.base import Base


class Rectangle(Base):
    """Inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.widtg = width
        self.height = height
        self.x = x
        sef.y = y

    @property
    def width(self):
        """Get width
        """
        return self.__width

    @width.setter
    def width(width, value):
        if type(value) != int:
            raise TypeError("width is not a integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("X must be an integer")
        if value <= 0:
            raise ValueError("X must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("Y must be an integer")
        if value <= 0:
            raise ValueError("Y must be > 0")

    def area(self):
        """Returns the area
        """
        return self.__width * self__height

    def display(self):
        """Return the ouput of the shape with '#'
           characters.
           
           y = is the newline
           x = is the space
        """
        if self.__y != 0:
            for newline in range(self.__y):
                print()

        for row in range(self.__height):
            print((self.__x * " ") + (self.__width * '#'))

    def __str__(self):
        """Formatted display
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update values
        """
        if len(kwargs) != 0:
            foi i, x in kwargs.items():
                setattr(self, i, x)
        elif len(args) != 0:
            try: 
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Dictionary representation
        """
        return {'id': self.__id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}

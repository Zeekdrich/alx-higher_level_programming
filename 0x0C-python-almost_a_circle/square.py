#!/usr/bin/python3
"""square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """set 'int' datatype
        """

        self.width = value
        self.height = value

    def __str__(self):
        """Return formatted display
        """

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        if len(kwargs) != 0:
            for x, i in kwargs.items():
                setattr(self, x, i)
            elif len(args) != 0:
                try:
                    self.id = args[0]
                    self.size = args[1]
                    self.x = args[2]
                    self.y = args[3]
                except IndexError:
                    pass
            else:
                print()

    def to_dictionary(self):
        """Dictionary representation
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

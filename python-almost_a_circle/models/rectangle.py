from base import Base
class Rectangle(Base):
    """Represents a polygon with 4 perpendicular and
    two pairs of equal sides.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle object.

        Args:
            width (int): The width of this rectangle.
            height (int): The height of this rectangle.
            x (int): The horizontal position of this rectangle.
            y (int): The vertical position of this rectangle.
            id (int): The id of this rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def width(self):
        """Gets or sets the width of this rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Gets or sets the height of this rectangle.
        """
        return self.__height

    @property
    def x(self):
        """Gets or sets the horizontal position of this rectangle.
        """
        return self.__x

    @property
    def y(self):
        """Gets or sets the vertical position of this rectangle.
        """
        return self.__y
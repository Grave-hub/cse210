class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
    """
    
    def __init__(self, x):
        """Constructs a new Point using the specified x value.
        
        Args:
            x (int): The specified x value.
        """
        self._x = x

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        return Point(x)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x()

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.
            
        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor)
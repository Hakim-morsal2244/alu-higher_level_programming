#!/usr/bin/python3
"""Square class that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the __str__ method to represent the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

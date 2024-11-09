# File: 100-my_int.py

class MyInt(int):
    """A rebellious integer class with inverted equality operators."""
    
    def __eq__(self, other):
        """Override == to act as !=."""
        return super().__ne__(other)
    
    def __ne__(self, other):
        """Override != to act as ==."""
        return super().__eq__(other)

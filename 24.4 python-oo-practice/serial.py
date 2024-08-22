"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initialize with a start number and set the current number to start.
        
        Args:
            start (int): The initial value of the serial number.
        """
        self.start = start
        self.current = start

    def generate(self):
        """Return the next serial number and increment the current number.
        
        Returns:
            int: The next serial number.
        """
        number = self.current
        self.current += 1
        return number

    def reset(self):
        """Reset the current serial number back to the starting number."""
        self.current = self.start

    def __repr__(self):
        """Show representation."""
        return f"<SerialGenerator start={self.start} current={self.current}>"
    


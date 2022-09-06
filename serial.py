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
    def __init__(self, start=0):
        self.start_number = start
        self.serial = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start_number} next={self.serial}>"
        

    def generate(self):
        """Generates the next serial number

        Returns:
            int: Increments serial number by 1
        """
        self.serial += 1
        return self.serial - 1
    
    def reset(self):
        """Resets serial number to start number
        """
        self.serial = self.start_number
    


serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())
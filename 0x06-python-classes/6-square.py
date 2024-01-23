class Square:
    """A class that defines a square by size and position.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square in 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the Square class with a size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square in 2D space. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #.

        Prints an empty line if size is equal to 0.
        Uses spaces for the position.
        """
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            print('\n'.join(' ' * self.__position[0] + '#' * self.__size for _ in range(self.__size)))


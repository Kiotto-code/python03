class calculator:
    """calculator class"""
    def __init__(self, number) -> None:
        """__init__"""
        self.data = number

    def __str__(self) -> str:
        """__str__"""
        return "Vector: ('{self.data}')"

    def __add__(self, object) -> None:
        """addition method"""
        self.data = [element + object for element in self.data]
        print(self.data)

    def __mul__(self, object) -> None:
        """multiplication method"""
        self.data = [element * object for element in self.data]
        print(self.data)

    def __sub__(self, object) -> None:
        """substraction method"""
        self.data = [element - object for element in self.data]
        print(self.data)

    def __truediv__(self, object) -> None:
        """true division method"""""
        if object == 0:
            print("ERROR (cannot divide by zero))")
            return
        self.data = [element / object for element in self.data]
        print(self.data)

class calculator:
    """calculator class"""
    @staticmethod
    def __init__(self, number) -> None:
        """__init__"""
        self.data = number

    @staticmethod
    def __str__(self) -> str:
        """__str__"""
        return "Vector: ('{self.data}')"

    @staticmethod
    def __add__(self, object) -> None:
        """addition method"""
        self.data = [element + 5 for element in self.data]
        print(self.data)

    @staticmethod
    def __mul__(self, object) -> None:
        """multiplication method"""
        self.data = [element * 5 for element in self.data]
        print(self.data)

    @staticmethod
    def __sub__(self, object) -> None:
        """substraction method"""
        self.data = [element - 5 for element in self.data]
        print(self.data)

    @staticmethod
    def __truediv__(self, object) -> None:
        """true division method"""""
        if object == 0:
            print("ERROR (div by zero)")
            return
        self.data = [element / 5 for element in self.data]
        print(self.data)

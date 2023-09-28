class calculator:
    """calculator class"""
    # def __init__ (self, number) -> None:
    #     """__init__"""
    #     self.data = number

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum([a * b for a, b in zip(V1, V2)])
        print("Dot product is:", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """addition method"""
        result = [float(a + b) for a, b in zip(V1, V2)]
        print("Add Vector is :", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """subtraction method"""
        result = [float(a - b) for a, b in zip(V1, V2)]
        print("Sous Vector is:", result)

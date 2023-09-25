from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King family."""
    def set_eyes(self, color):
        """eyes color setter"""
        self.eyes = color

    def get_eyes(self):
        """eyes color getter"""
        return self.eyes

    def set_hairs(self, color):
        """hairs color setter"""
        self.hairs = color

    def get_hairs(self):
        """hairs color getter"""
        return self.hairs

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True, family_name="Baratheon",
                 eyes="brown", hairs="dark"):
        """Character class __init__ method"""
        # self.first_name = first_name
        # self.is_alive = is_alive
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Abstract method for dying"""
        self.is_alive = False

    def __repr__(self):
        """Return a string representation of the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self) -> str:
        return self.__repr__(self)


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True, family_name="Lannister",
                 eyes="blue", hairs="light"):
        """Character class __init__ method"""
        # self.first_name = first_name
        # self.is_alive = is_alive
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Abstract method for dying"""
        self.is_alive = False

    @classmethod
    def create_lannister(self, first_name, is_alive=True):
        """Create a Lannister"""
        return Lannister(first_name, is_alive)

    def __repr__(self):
        """Return a string representation of the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self) -> str:
        return self.__repr__()

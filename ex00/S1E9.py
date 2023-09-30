from abc import ABC, abstractmethod


class Character(ABC):
    """Character template for student in S1E9"""
    def __init__(self, first_name, is_alive=True):
        """Character class __init__ method"""
        self.first_name = first_name
        self.is_alive = is_alive
        # self.family_name = None
        # self.eyes = None
        # self.hairs = None

    @abstractmethod
    def die(self):
        """Abstract method for dying"""
        pass


class Stark(Character):
    """Class for Student in S1E9"""
    def die(self):
        """Abstract method for dying"""
        self.is_alive = False

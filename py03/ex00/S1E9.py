from abc import ABC, abstractmethod


class Character(ABC):
    """docstring for Character"""
    def __init__(self, first_name, is_alive=True):
        """docstring for Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """docstring for die method in Character class"""
        pass


class Stark(Character):
    """docstring for Stark"""
    def die(self):
        """docstring for die method in Stark class"""
        self.is_alive = False

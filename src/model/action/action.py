from abc import ABC, abstractmethod
from src.model.communication.physical.robot import Robot

class Action(ABC):

    @abstractmethod
    def dictify(self, robots: list[Robot]) -> dict:
        pass
    
    @abstractmethod
    def dictify_to_display(self, robots: list[Robot]) -> dict:
        pass
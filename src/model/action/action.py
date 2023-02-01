from abc import ABC, abstractmethod

class Action(ABC):

    @abstractmethod
    def dictify(self) -> dict:
        pass
from abc import ABC, abstractmethod


class PathObserver(ABC):

    @abstractmethod
    def update(self, path):
        pass

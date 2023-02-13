from abc import ABC, abstractmethod


class PathObserver(ABC):

    @abstractmethod
    def update_path(self, path):
        pass

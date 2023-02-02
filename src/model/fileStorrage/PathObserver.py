from abc import ABC

class PathObserver(ABC):

    def update(self, path):
        self.path = path



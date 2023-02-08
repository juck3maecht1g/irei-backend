from abc import ABC, abstractmethod

class FileInterface(ABC):

    def __init__(self, path: str, file_name: str, data: dict):
        self.path = path
        self.file_name = file_name
        self.data = data
        
    @abstractmethod
    def create():
        pass


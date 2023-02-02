from abc import ABC, abstractmethod

class FileInterface(ABC):


    def __init__(self, file_name, data, path):
        self.file_name = file_name
        self.data = data
        self.path = path

    @abstractmethod
    def create():
        pass


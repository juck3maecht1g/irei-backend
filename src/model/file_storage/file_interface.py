from abc import ABC, abstractmethod


class FileInterface(ABC):

    def __init__(self, path: str, file_name: str, file_name_extension: str, data: dict):
        self.path = path
        self.file_name_extension = file_name_extension
        self.file_name = file_name
        self.data = data

    def get_extended_name(self):
        return self.file_name + self.file_name_extension

    def _make_extended_name(self, name: str):
        return name + self.file_name_extension

    @abstractmethod
    def create():
        pass

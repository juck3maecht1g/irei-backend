from abc import ABC

class Coordinate(ABC):
    def __init__(self, coord: dict):
        self.coord = coord

    def get_coordinate(self) -> dict:
        return self.coord

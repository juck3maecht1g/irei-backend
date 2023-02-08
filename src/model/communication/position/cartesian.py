from src.model.communication.position.coordinate import Coordinate

class Cartesian(Coordinate):
    def __init__(self, coord: dict):
        if (len(coord['coord']) == 3 and len(coord['quat']) == 4):
            super().__init__(coord)
        else:
            raise ValueError(f'Cannot parse {coord} to joint coordinate.')

    def get_coord(self) -> dict:
        return self.coord["coord"]

    def get_quat(self) -> dict:
        return self.coord["quat"]

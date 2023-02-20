from src.model.communication.position.coordinate import Coordinate
import numpy as np

class Cartesian(Coordinate):
    def __init__(self, coord: dict):
        if (len(coord['coord']) == 3 and len(coord['quat']) == 4):
            coord["coord"] = np.array(coord["coord"]).tolist()
            coord["quat"] = np.array(coord["quat"]).tolist()
            super().__init__(coord)
        else:
            raise ValueError(f'Cannot parse {coord} to joint coordinate.')

    def get_coord(self) -> list[int]:
        return self.coord["coord"]

    def get_quat(self) -> list[int]:
        return self.coord["quat"]

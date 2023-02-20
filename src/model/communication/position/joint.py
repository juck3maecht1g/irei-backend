from src.model.communication.position.coordinate import Coordinate
import numpy as np

class Joint(Coordinate):
    def __init__(self, coord: dict):
        if (len(coord["values"]) == 7):
            coord["values"] = np.array(coord["values"]).tolist()
            super().__init__(coord)    
        else:
            raise ValueError(f'Cannot parse {coord} to joint coordinate.')
        

    def get_values(self) -> list[float]:
        return self.coord["values"]

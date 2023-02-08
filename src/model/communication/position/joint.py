from src.model.communication.position.coordinate import Coordinate

class Joint(Coordinate):
    def __init__(self, coord: dict):
        if (len(coord["values"]) == 7):
            super().__init__(coord)    
        else:
            raise ValueError(f'Cannot parse {coord} to joint coordinate.')

    

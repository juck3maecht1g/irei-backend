from src.model.communication.position.coordinate import Coordinate

class Cartesian(Coordinate):
    def __init__(self, coord: dict):
        if not (coord.get('space') == 'cartesian' and len(coord.get('coords')) == 3 and len(coord.get('quat')) == 4):
            raise ValueError(f'Cannot parse {coord} to joint coordinate.')
        else:
            super(coord)


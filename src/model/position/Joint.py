from Coordinate import Coordinate

class Joint(Coordinate):
    def __init__(self, coord: dict):
        if not (coord.get('space') == 'joint' and len(coord.get('values')) == 7):
            raise ValueError(f'Cannot parse {coord} to joint coordinate.')
        else:
            super(coord)

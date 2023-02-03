from src.model.communication.position.cartesian import Cartesian
from src.model.communication.position.joint import Joint

class Position:
    def __init__(self, name: str, cartesian: Cartesian, joint: Joint):
        self.cartesian = cartesian
        self.joint = joint
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_coordinate(self, type: str):
        if type == "cartesian":
            return self.cartesian.get_coordinate()
        elif type == "joint":
            return self.joint.get_coordinate()
        else:
            return

    def get_name(self):
        return self.name

from Cartesian import Cartesian
from Joint import Joint
from datetime import datetime

class Position:
    def __init__(self, name: str, cartesian: Cartesian, joint: Joint):
        self.cartesian = cartesian
        self.joint = joint
        if name == None:
            self.name = str(datetime.now())
        self.name = name
        self.is_cartesian = False

    def set_name(self, name):
        self.name = name

    def get_coordinate(self):
        return self.cartesian.get_coordinate() if self.is_cartesian else self.joint.get_coordinate() 

    def get_name(self):
        return self.name

    def switch_space(self):
        self.is_cartesian = not self.is_cartesian

    def get_is_cartesian(self):
        return self.is_cartesian

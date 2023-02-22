from src.model.communication.position.cartesian import Cartesian
from src.model.communication.position.joint import Joint
from src.model.communication.position.coordinate import Coordinate
from copy import copy


class Variable:
    def __init__(self, data: dict):
        name = list(data.keys())[0]
        self.name = name
        self.cartesian = Cartesian(data[name]["cartesian"])
        self.joint = Joint(data[name]["joint"])

    def set_name(self, name) -> str:
        self.name = name

    def get_coordinate(self, type: str) -> Coordinate:
        if type == "cartesian":
            return self.get_cartesian()
        elif type == "joint":
            return self.get_joint()

    def to_dict(self) -> dict:
        out = {self.name: {
            "cartesian": {
                "coord": self.cartesian.get_coord(),
                "quat": self.cartesian.get_quat()
            },
            "joint": {
                "values": self.joint.get_values()
            }
        }
        }
        return copy(out)

    def get_name(self) -> str:
        return self.name

    def get_used_space(self) -> str:
        return self.used_space

    def get_cartesian(self) -> dict:
        to_return = {"coord": self.cartesian.get_coord(), "quat": self.cartesian.get_quat()}
        return to_return

    def get_joint(self) -> dict:
        return {"values": self.joint.get_values()}
    
    def get_name(self) -> str:
        return self.name

    def __eq__(self, obj):
        return isinstance(obj, Variable) and self.to_dict() == obj.to_dict()

from src.model.communication.position.cartesian import Cartesian
from src.model.communication.position.joint import Joint
from src.model.communication.position.coordinate import Coordinate


class Variable:
    def __init__(self, data: dict):
        name = list(data.keys())[0]
        self.name = name
        self.used_space = data["used space"]
        self.cartesian = Cartesian(data["cartesian"])
        self.joint = Joint(data["joint"])

    def set_name(self, name) -> str:
        self.name = name

    def get_coordinate(self) -> Coordinate:
        if self.used_space == "cartesian":
            return self.get_cartesian()
        elif self.used_space == "joint":
            return self.get_joint()

    def to_dict(self) -> dict:
        out = {self.name: {
            "used space": self.used_space,
            "cartesian": {
                "coord": self.cartesian.get_coord(),
                "quat": self.cartesian.get_quat()
            },
            "joint": {
                "values": self.get_joint()["values"]
            }
        }
        }
        return out

    def get_name(self) -> str:
        return self.name

    def get_used_space(self) -> str:
        return self.used_space

    def get_cartesian(self) -> Cartesian:
        return self.cartesian.get_coordinate()

    def get_joint(self) -> Joint:
        return self.joint.get_coordinate()

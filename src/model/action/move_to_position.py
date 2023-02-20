from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot
from src.model.communication.position.variable import Variable


class MoveToPosition(ListableAction):
    key: str = "move"

    def __init__(self, robot_nrs: list[int], name, coord, type: str) -> None:
        super().__init__(robot_nrs)
        self.name = name
        self.coord = coord
        self.type = type

    def map_dictify(self, map: dict) -> dict:
        to_return = dict()
        to_return["key"] = MoveToPosition.key
        to_return["name"] = self.name
        to_return["type"] = self.type
        to_return["coord"] = self.coord
        to_return |= super().map_dictify(map)
        return to_return

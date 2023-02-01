from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot


class MoveToPosition(ListableAction):
    key: str = "move"

    def __init__(self, robot_nrs: list[int], coordinates: dict, type: str) -> None:
        super(robot_nrs)
        self.coordinates = coordinates
        self.type = type

    def dictify(self, robots: list[Robot]) -> dict:
        to_return = dict()
        to_return["key"] = MoveToPosition.key
        to_return["robots"] = self.map_robots(self.robot_nrs, robots)
        to_return["type"] = self.type
        to_return["coordiantes"] = self.coordinates
        return to_return

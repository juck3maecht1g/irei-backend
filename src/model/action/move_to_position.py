from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot
from src.model.communication.position.variable import Position


class MoveToPosition(ListableAction):
    key: str = "move"

    def __init__(self, robot_nrs: list[int], position: Position, type: str) -> None:
        super(robot_nrs)
        self.position = position
        self.type = type

    def dictify(self, robots: list[Robot]) -> dict:
        to_return = dict()
        to_return["key"] = MoveToPosition.key
        to_return["robots"] = super().map_robots(self.robot_nrs, robots)
        to_return["type"] = self.type
        to_return["coordiante"] = self.position.get_coordinate(self.type)
        return to_return

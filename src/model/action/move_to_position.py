from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot
from src.model.communication.position.variable import Variable


class MoveToPosition(ListableAction):
    key: str = "move"

    def __init__(self, robot_nrs: list[int], position: Variable) -> None:
        super().__init__(robot_nrs)
        self.position = position
        self.type = position.get_used_space()

    def dictify(self, robots: list[Robot]) -> dict:
        to_return = dict()
        to_return["key"] = MoveToPosition.key
        to_return["name"] = self.position.get_name()
        to_return["robots"] = super().map_robots(self.robot_nrs, robots)
        to_return["type"] = self.type
        to_return["coord"] = self.position.get_coordinate()
        return to_return

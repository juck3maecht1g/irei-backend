from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot


class OpenGripper(ListableAction):
    key: str = "open_gripper"

    def __init__(self, robot_nrs: list[int]) -> None:
        super().__init__(robot_nrs)

    def map_dictify(self, robots: list[Robot]) -> dict:
        to_return = dict()
        to_return["key"] = OpenGripper.key
        to_return["robots"] = super().map_robots(self.robot_nrs, robots)
        return to_return

    def map_dictify(self, map: dict) -> dict:
        to_return = dict()
        to_return["key"] = OpenGripper.key
        to_return |= super().map_dictify(map)
        return to_return

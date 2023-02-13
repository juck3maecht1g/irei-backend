from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot


class CloseGripper(ListableAction):
    key: str = "close_gripper"

    def __init__(self, robot_nrs: list[int]) -> None:
        super().__init__(robot_nrs)

    def dictify(self, robots: list[Robot], use_numbers=False) -> dict:
        to_return = dict()
        to_return["key"] = CloseGripper.key
        if use_numbers:
            to_return["robots"] = super().map_robots(self.robot_nrs, robots)
        else:
            to_return["robots"] = self.robot_nrs
        return to_return

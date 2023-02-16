from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot



class CloseGripper(ListableAction):
    key: str = "close_gripper"

    def __init__(self, robot_nrs: list[int]) -> None:
        super().__init__(robot_nrs)

    def map_dictify(self, map: dict) -> dict:
        to_return = dict()
        to_return["key"] = CloseGripper.key
        to_return |= super().map_dictify(map)
        return to_return

    
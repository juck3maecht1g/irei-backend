from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot


class Wait(ListableAction):
    key: str = "wait"

    def __init__(self, robot_nrs: list[int], time: int) -> None:
        super().__init__(robot_nrs)
        self.time = time

    def map_dictify(self, map: dict) -> dict:
        to_return = dict()
        to_return["key"] = Wait.key
        to_return["time"] = self.time
        to_return |= super().map_dictify(map)
        return to_return

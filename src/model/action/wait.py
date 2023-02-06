from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot


class Wait(ListableAction):
    key: str = "wait"

    def __init__(self, robot_nrs: list[int], time: int) -> None:
        super().__init__(robot_nrs)
        self.time = time

    def dictify(self, robots: list[Robot]) -> dict:
        to_return = dict()
        to_return["key"] = Wait.key
        to_return["robots"] = self.map_robots(self.robot_nrs, robots)
        to_return["time"] = self.time
        return to_return

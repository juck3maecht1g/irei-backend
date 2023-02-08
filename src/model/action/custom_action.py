from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot


class CustomAction(ListableAction):
    key: str = "custom"

    def __init__(self, robot_nrs: list[int], action: str) -> None:
        super().__init__(robot_nrs)
        self.action = action

    def dictify(self, robots: list[Robot]) -> dict:
        to_return = dict()
        to_return["key"] = CustomAction.key
        to_return["robots"] = super().map_robots(self.robot_nrs, robots)
        to_return["action"] = self.action
        return to_return

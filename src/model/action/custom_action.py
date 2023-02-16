from src.model.action.listable_action import ListableAction
from src.model.communication.physical.robot import Robot


class CustomAction(ListableAction):
    key: str = "custom"

    def __init__(self, robot_nrs: list[int], action: str) -> None:
        print("\nwhere????????????")
        super().__init__(robot_nrs)
        self.action = action

    def map_dictify(self, map: dict) -> dict:
        to_return = dict()
        to_return["key"] = CustomAction.key
        to_return["action"] = self.action
        to_return |= super().map_dictify(map)
        return to_return

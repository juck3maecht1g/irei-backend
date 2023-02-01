from src.model.action.listable_action import ListableAction


class CustomAction(ListableAction):
    key: str = "custom"

    def __init__(self, robot_nrs: list[int], action: str) -> None:
        super(robot_nrs)
        self.action = action

    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = CustomAction.key
        to_return["robot_nrs"] = self.get_robot_nrs()
        to_return["action"] = self.action
        return to_return
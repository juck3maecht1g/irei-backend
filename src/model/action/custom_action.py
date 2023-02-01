from src.model.action.listable_action import ListableAction


class CustomAction(ListableAction):
    key: str = "custom"

    def __init__(self, robot_nr: int, action: str) -> None:
        self.robot_nr = robot_nr
        self.action = action



    def get_robot_nr(self) -> int:
        return self.robot_nr
    


    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = CustomAction.key
        to_return["robot_nr"] = self.robot_nr
        to_return["action"] = self.action
        return to_return
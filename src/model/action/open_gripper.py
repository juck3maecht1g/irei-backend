from src.model.action.listable_action import ListableAction


class OpenGripper(ListableAction):
    key: str = "open_gripper"

    def __init__(self, robot_nrs: list[int]) -> None: 
        super(robot_nrs)
      
    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = OpenGripper.key
        to_return["robot_nrs"] = self.get_robot_nrs()
        return to_return
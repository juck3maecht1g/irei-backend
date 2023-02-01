from src.model.action.listable_action import ListableAction


class OpenGripper(ListableAction):
    key: str = "open_gripper"

    def __init__(self, robot_nr: int) -> None: 
        self.robot_nr = robot_nr
      



    def get_robot_nr(self) -> int:
        return self.robot_nr
    


    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = OpenGripper.key
        to_return["robot_nr"] = self.robot_nr
        return to_return
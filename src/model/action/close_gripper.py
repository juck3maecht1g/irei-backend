from src.model.action.listable_action import ListableAction

class CloseGripper(ListableAction):
    key: str = "close_gripper"

    def __init__(self, robot_nrs: list[int]) -> None: 
        super(robot_nrs)
    
    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = CloseGripper.key
        to_return["robot_nrs"] = self.get_robot_nrs()
        return to_return
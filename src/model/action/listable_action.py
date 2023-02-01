from src.model.action.action import Action


class ListableAction(Action):
    
    def __init__(self, robot_nrs: list[int]) -> None:
        self.robot_nrs = robot_nrs

    def get_robot_nrs(self) -> list[int]:
        return self.robot_nrs
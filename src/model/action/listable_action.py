from src.model.action.action import Action
from src.model.communication.physical.robot import Robot


class ListableAction(Action):
    
    def __init__(self, exe_robots: list[Robot]) -> None:
        self.exe_robots = exe_robots

    def get_exe_robots(self) -> list[Robot]:
        return self.exe_robots
    

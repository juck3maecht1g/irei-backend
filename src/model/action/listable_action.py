from abc import abstractmethod

from src.model.action.action import Action
from src.model.communication.physical.robot import Robot


class ListableAction(Action):

    def __init__(self, robot_nrs: list[int]) -> None:
        self.robot_nrs = robot_nrs

    def get_robot_nrs(self) -> list[int]:
        return self.robot_nrs

    def map_robots(robot_nrs: list[int], robot_list: list[Robot]) -> dict:
        robots_dict = []
        for robot_nr in robot_nrs():
            robots_dict.append(
                {"name": robot_list[robot_nr].get_name(), "ip": robot_list[robot_nr].get_ip()})
        return robots_dict

    @abstractmethod
    def dictify(self, robots: list[Robot]) -> dict:
        pass

    def dictify_to_display(self, robots: list[Robot]) -> dict:
        return self.dictify(robots)

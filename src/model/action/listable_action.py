from abc import abstractmethod

from src.model.action.action import Action
from src.model.communication.physical.robot import Robot


class ListableAction(Action):

    def __init__(self, robot_nrs: list[int]) -> None:
        self.key = ""
        self.robot_nrs = robot_nrs

    def get_robot_nrs(self) -> list[int]:  # useless?
        return self.robot_nrs


    def map_dictify(self, map: dict) -> dict:
        to_return = dict()
        if map is None:
            to_return["robots"] = self.robot_nrs
        else:
            new_ip = []
            for rob in self.robot_nrs:
                new_ip.append(map[rob])
            to_return["robots"] = new_ip
            
        return to_return

    def nr_dictify(self) -> dict:
        to_return = self.map_dictify(None)
        to_return["robot_nrs"] = self.robot_nrs
        return to_return


    def dictify_to_display(self, map):
        return self.map_dictify(map)

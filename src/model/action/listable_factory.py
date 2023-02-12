from close_gripper import CloseGripper
from custom_action import CustomAction
from move_to_position import MoveToPosition
from open_gripper import OpenGripper
from wait import Wait


class ListableFactory:

    @staticmethod
    def create_single_action(action: dict) -> None:
        if action["key"] == "close_gripper":
            return CloseGripper(action["robot_nrs"])
        elif action["key"] == "custom":
            return CustomAction(action["robot_nrs"], action["action"])
        elif action["key"] == "move":
            return MoveToPosition(action["robot_nrs"], action["position"], action["type"])
        elif action["key"] == "open_gripper":
            return OpenGripper(action["robot_nrs"])
        elif action["key"] == "wait":
            return Wait(action["robot_nrs"], action["time"])

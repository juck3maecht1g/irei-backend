
from src.model.action.custom_action import CustomAction
from src.model.action.move_to_position import MoveToPosition
from src.model.action.open_gripper import OpenGripper
from src.model.action.close_gripper import CloseGripper
from src.model.action.wait import Wait


class ListableFactory:
    
    @staticmethod
    @staticmethod
    def create_single_action(action: dict) -> None:
        print("listableFaktory", action)
        if action["key"] == "close_gripper":
            return CloseGripper(action["robot_nrs"])
        elif action["key"] == "custom":
            return CustomAction(action["robot_nrs"], action["action"])
        elif action["key"] == "move":
            return MoveToPosition(action["robot_nrs"], action["position"])
        elif action["key"] == "open_gripper":
            return OpenGripper(action["robot_nrs"])
        elif action["key"] == "wait":
            return Wait(action["robot_nrs"], action["time"])

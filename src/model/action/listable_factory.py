from close_gripper import CloseGripper
from custom_aktion import CustomAction
from move_to_position import MoveToPosition
from open_gripper import OpenGripper
from wait import Wait

class ListableFactory:

    def create_single_action(action :dict) :
        if action.key == "close_gripper" :
                return CloseGripper(action.robot_nr)
        elif action.key == "custom":
                return CustomAction(action.robot_nr, action.action)
        elif action.key == "move" :
                return MoveToPosition(action.robot_nr, action.coordinates, action.is_cartesian)
        elif action.key == "open_gripper":
                return OpenGripper(action.robot_nr)
        elif action.key == "wait":
                return Wait(action.robot_nr, action.time)
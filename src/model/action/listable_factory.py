from close_gripper import CloseGripper
from custom_aktion import CustomAction
from move_to_position import MoveToPosition
from open_gripper import OpenGripper
from wait import Wait

class ListableFactory:

    def create_single_action(action :dict) :
        match action.key:
            case "close_gripper":
                return CloseGripper(action.robot_nr)
            case "custom":
                return CustomAction(action.robot_nr, action.action)
            case "move" :
                return MoveToPosition(action.robot_nr, action.coordinates, action.is_cartesian)
            case "open_gripper":
                return OpenGripper(action.robot_nr)
            case "wait":
                return Wait(action.robot_nr, action.time)
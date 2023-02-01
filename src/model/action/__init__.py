from src.model.action.close_gripper import CloseGripper
from src.model.communication.physical.robot import Robot


print(CloseGripper([1]).dictify_to_display([Robot("q", "a"), Robot("1", "2")]))
from src.model.action.close_gripper import CloseGripper
from src.model.action.open_gripper import OpenGripper
from src.model.action.action import Action
from src.model.action.listable_action import ListableAction
from src.model.action.action_list import ActionList
from src.model.action.wait import Wait
from src.model.action.move_to_position import MoveToPosition
from src.model.action.custom_action import CustomAction
from src.model.communication.physical.robot import Robot
from src.model.communication.position.joint import Joint
from src.model.communication.position.cartesian import Cartesian
from src.model.communication.position.variable import Variable
from src.root_dir import root_path

map = {0: "ip1", 1: "ip2", 2: "ip2","sublist": [{0: "ip00", 1: "ip22"}]}

time = 10
og1 = CloseGripper([1])
cg1 = CloseGripper([1])
al1 = ActionList("first_list", "sequential_list")
al2 = ActionList("second_list", "parallel_list")
w = CloseGripper([1])
#mp = MoveToPosition([1], pos, "joint")
ca = CloseGripper([1])
b = CloseGripper([0])
c = CloseGripper([2])
al2.add_action(b)
al2.add_action(w)
al1.add_action(ca)
al1.add_action(b)
al1.add_action(al2)
al1.add_action(ca)
al1.add_action(c)
print(al1.map_dictify(map))
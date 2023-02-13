"""from src.controller.irei import *
from src.model.communication.physical.robot import Robot
class TestClass:
    def __init__():
        pass
    
robots = [Robot("q", "a"), Robot("1", "2")]

register_experiment(TestClass)
setup_experiment("experiment", robots)
initialize()
"""
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

from src.controller.irei import *
class TestClass:
    def __init__():
        pass
    
register_experiment(TestClass)
setup_experiment("experiment")
initialize(root_path)

"""
robots = [Robot("q", "a"), Robot("1", "2")]

var_dict = ({"name": "var1", "joint": {"values": [1, 0, 0, 0, 0, 0, 0]}, "used space": "joint", "cartesian": {
            "coord": [1, 0, 0], "quat": [1, 0, 0, 0]}})
#pos = Variable(var_dict)
time = 10
og1 = OpenGripper([1])
cg1 = CloseGripper([1])
al1 = ActionList("list1", "sequential")
al2 = ActionList("list1", "parallel")
w = Wait([1], time)
#mp = MoveToPosition([1], pos, "joint")
ca = CustomAction([1], "stupid action")
al2.add_action(og1)
al2.add_action(w)
al1.add_action(ca)
al1.add_action(al2)

print(cg1.dictify_to_display(robots))
print(og1.dictify_to_display(robots))
print(al1.dictify_to_display(robots))
print(w.dictify_to_display(robots))
#print(mp.dictify_to_display(robots))  # in dev
print(ca.dictify_to_display(robots))

print("\n dictify")
print(al1.dictify(robots))
print("display")
print(al1.dictify_to_display(robots))


def test_sth():
    assert time == int(w.dictify_to_display(robots)["time"])
#"""
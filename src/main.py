"""from src.controller.irei import *
class TestClass:
    def __init__():
        pass
    
register_experiment(TestClass)
setup_experiment("experiment")
initialize()"""

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
from src.model.communication.position.position import Position

import pytest

robots = [Robot("q", "a"), Robot("1", "2")]

j_c = Joint(dict({"space": "joint", "values": [1, 0, 0, 0, 0, 0, 0]}))
c_c = Cartesian(dict({"space": "cartesian", "coords": [
                1, 0, 0], "quat": [1, 0, 0, 0]}))  # check for none
pos = Position(name="pos1", cartesian=c_c, joint=j_c)
time = 10
og1 = OpenGripper([1])
cg1 = CloseGripper([1])
al1 = ActionList("list1", "sequential")
al2 = ActionList("list1", "parallel")
w = Wait([1], time)
mp = MoveToPosition([1], pos, "joint")
ca = CustomAction([1], "stupid action")
al2.add_action(og1)
al2.add_action(w)
al1.add_action(ca)
al1.add_action(al2)

print(cg1.dictify_to_display(robots))
print(og1.dictify_to_display(robots))
print(al1.dictify_to_display(robots))
print(w.dictify_to_display(robots))
print(mp.dictify_to_display(robots))  # in dev
print(ca.dictify_to_display(robots))

print("\n dictify")
print(al1.dictify(robots))
print("display")
print(al1.dictify_to_display(robots))


def test_sth():
    assert time == int(w.dictify_to_display(robots)["time"])

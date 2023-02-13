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
"""
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
al1 = ActionList("first_list", "sequential")
al2 = ActionList("second_list", "parallel")
w = Wait([1], time)
#mp = MoveToPosition([1], pos, "joint")
ca = CustomAction([1], "stupid action")
al2.add_action(og1)
al2.add_action(w)
al1.add_action(ca)
al1.add_action(ca)
al1.add_action(al2)
al1.add_action(ca)

def tree(action_list: ActionList):
    to_return = dict()
    to_return["name"] = action_list.name
    to_return["mapping"] = []
    for c in range(0, len(action_list.get_content())):
        if not isinstance(action_list.get_content()[c], ActionList):
            temp = dict()
            temp["name"] = "action"
            temp["robot"] = c
            to_return["mapping"].append(temp)
        else: 
            to_return["mapping"].append(tree(action_list.get_content()[c]))
    return to_return

    print(tree(al1))




def detree(action_list: ActionList, mapping,):
    to_return = []
    lookup = mapping["mapping"]
    for c in range(0, len(action_list.get_content())):
        if not isinstance(action_list.get_content()[c], ActionList):
           to_return.append("this is a simple action " + str(c))  #action_list.get_content()[c].dictify(mapping["mapping"][c]["robot"]) auskommentiert weil sonst robotter mappen nötig
        else: 
            to_return.append(detree(action_list.get_content()[c], lookup[c]))
            
    return to_return

print(detree(al1, tree(al1)))
"""
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
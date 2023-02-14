from src.model.communication.physical.robot import Robot
from src.model.communication.position.variable import Variable
from src.model.file_storage.yaml_file import YamlFile
from src.model.file_storage.path_observer import PathObserver
from src.model.communication.physical.robot import Robot
from src.model.action.action_list import ActionList
from src.model.action.action import Action
from src.model.action.listable_factory import ListableFactory



import os

# todo Observer


class ActionListHandler(YamlFile, PathObserver):

    folder_name = "Action Lists"


    def __init__(self, root: str):
        
        self.data = {
            "type": "sequential",
            "content": [{"key": "open_gripper", "robot_nrs": [1]}]
        }
        #TODO 
        super().__init__(root, None, self.data)
        self.root = root


    def create(self, name: str):
        self.file_name = name
        parent_path = os.path.dirname(self.path)

        if not (self.path == self.root):

            if not (ActionListHandler.folder_name in os.listdir(parent_path)):
                os.mkdir(self.path)

            if not (name in os.listdir(self.path)):
                self.write()

    def update_path(self, path):
        self.path = os.path.join(path, ActionListHandler.folder_name)


    def get_lists(self) -> list[str]:
        return os.listdir(self.path)

    def get_list(self, name) -> ActionList:
        sublist = 0
        self.file_name = name
        self.read()
        out = ActionList(name, self.data["type"])
        for action in self.data["content"]:
            if action["key"] == "file":
                out.add_action(self.get_list(action["name"]))
                sublist += 1
                self.file_name = name
            else:
                out.add_action(ListableFactory.create_single_action(action))
        return out

    def add_action(self, name, action: Action):
        self.file_name = name
        self.read()
        new = action.dictify_to_display(None)
        if "list" in new["key"]:
            new["key"] = "file"
            new["name"] = action.dictify_to_display()["name"]
        self.data["content"].append(new)
        self.write()

    def del_action(self, name: str, index: int) -> bool:
        self.file_name = name
        self.read()
        self.data["content"].pop(index)
        self.write()

    def swap_action(self, name: str, index1: int, index2: int) -> bool:
        self.file_name = name
        self.read()
        temp = self.data["content"][index1]
        self.data["content"][index1] = self.data["content"][index2]
        self.data["content"][index2] = temp
        self.write()

    

    
   
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
            "type": "sequential_list",
            "content": []
        }
        #TODO 
        super().__init__(root, None, self.data)
        self.root = root

    def __folder_exists(self):
        if os.path.dirname(self.path) == self.root:
            raise ValueError(f"There can't be an action list in your root path: {self.root}")
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def __is_list(self, name):
        self.__folder_exists()
        if not name in os.listdir(self.path):
            raise ValueError(f"There is no action list named {name} in {self.path}")
        
        self.file_name = name
        self.read()

    def create(self, name: str, type: str):
        print("\n\n"), print(name)
        self.file_name = name

        self.__folder_exists()
        if (name in os.listdir(self.path)):
            raise ValueError(f"There is already an action list named {name} in {self.path}")
            
        self.data["type"] = type
        self.write()
            

    def update_path(self, path):
        self.path = os.path.join(path, ActionListHandler.folder_name)


    def get_lists(self) -> list[str]:
        self.__folder_exists()
        return os.listdir(self.path)

    def get_list(self, name: str) -> ActionList:
        print("name it" ,name)
        sublist = 0
        self.__is_list(name)
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
        self.__is_list(name)
        new = action.nr_dictify()
        if "list" in new["key"]:
            new_name = action.nr_dictify()["name"]
            if not new_name == name:
                if new_name in os.listdir(self.path):
                    new["key"] = "file"
                    del new["content"]
                    new["name"] = new_name
                else:
                    raise ValueError(f"There is no saved action list with the name {name} in {self.path}.")
            else:
                raise ValueError(f"An action list must not contain itself.")
        self.data["content"].append(new)
        self.write()

    def print(self, name):
        self.__is_list(name)
        print(self.data)

    def del_action(self, name: str, index: int) -> bool:
        self.__is_list(name)
        self.data["content"].pop(index)
        self.write()

    def swap_action(self, name: str, index1: int, index2: int) -> bool:
        self.__is_list(name)
        temp = self.data["content"][index1]
        self.data["content"][index1] = self.data["content"][index2]
        self.data["content"][index2] = temp
        self.write()


    
   
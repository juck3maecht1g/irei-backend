from src.model.file_storage.yaml_file import YamlFile
from src.model.file_storage.path_observer import PathObserver
from src.model.action.action_list import ActionList
from src.model.action.action import Action
from src.model.action.listable_factory import ListableFactory
from src.resources.config_default.action_list_values import AlValues
from src.resources.errors.file_errors import FileNotAllowedInRootError, FileNotExistsError, FileNameAlreadyUsedError
from src.resources.errors.action_list_errors import IndexOutOfBoundsError



import os


#todo kreiserror
class ActionListHandler(YamlFile, PathObserver):

    def __init__(self, root: str):
        super().__init__(root, None, AlValues.DEFAULT_DATA.value)
        self.root = root

    def __folder_exists(self):
        if os.path.dirname(self.path) == self.root:
            raise FileNotAllowedInRootError(AlValues.ERROR_FOLDER_NAME.value, self.root)
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def __is_list(self, name):
        self.__folder_exists()
        if not self._make_extended_name(name) in os.listdir(self.path):
            raise FileNotExistsError(self._make_extended_name(name), self.path)
        
        self.file_name = name
        self.read()


    def create(self, name: str, type: str):
        self.file_name = name
        self.__folder_exists()
        if not (self._make_extended_name(name) in os.listdir(self.path)):
            self.data = AlValues.DEFAULT_DATA.value   
            self.data[AlValues.TYPE.value] = type
            self.write()
        else:
            raise FileNameAlreadyUsedError(name, self.path)
            

    def update_path(self, path):
        self.path = os.path.join(path, AlValues.FOLDER_NAME.value)


    def get_lists(self) -> list[str]:
        self.__folder_exists()
        return [os.path.splitext(filename)[0] for filename in os.listdir(self.path)]

    def get_list(self, name: str) -> ActionList:
        sublist = 0
        self.__is_list(name)
        self.file_name = name
        self.read()   
        out = ActionList(name, self.data[AlValues.TYPE.value])
        for action in self.data[AlValues.CONTENT.value]:
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
                if self._make_extended_name(new_name) in os.listdir(self.path):
                    new["key"] = "file"
                    del new["content"]
                    new["name"] = new_name
                else:
                    raise FileNotExistsError(self._make_extended_name(new_name), self.path)
            else:
                raise ValueError(f"An action list must not contain itself.")

        self.data[AlValues.CONTENT.value].append(new)
        self.write()


    def del_action(self, name: str, index: int) -> bool:
        self.__is_list(name)
        if index <= (len(self.data[AlValues.CONTENT.value]) - 1) and index >= 0:
            self.data[AlValues.CONTENT.value].pop(index)
            self.write()
        else:
            raise IndexOutOfBoundsError([index], len(self.data[AlValues.CONTENT.value]))

    def swap_action(self, name: str, index1: int, index2: int) -> bool:
        self.__is_list(name)
        highest_index = len(self.data[AlValues.CONTENT.value]) - 1
        if index1 <= highest_index and index2 <= highest_index and index1 >= 0 and index2 >= 0:
            temp = self.data[AlValues.CONTENT.value][index1]
            self.data[AlValues.CONTENT.value][index1] = self.data[AlValues.CONTENT.value][index2]
            self.data[AlValues.CONTENT.value][index2] = temp
            self.write()
        else:
            raise IndexOutOfBoundsError([index1, index2], len(self.data[AlValues.CONTENT.value]))
            
    
   
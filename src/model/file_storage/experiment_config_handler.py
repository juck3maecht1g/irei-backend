from src.model.communication.physical.robot import Robot
from src.model.communication.position.variable import Variable
from src.model.file_storage.yaml_file import YamlFile
from src.model.file_storage.path_observer import PathObserver

from src.resources.config_default.experiment_config_values import ExpConfigValues
from src.resources.errors.file_errors import FileNameAlreadyUsedError, FileNotAllowedInRootError

import os

# todo Observer


class ExperimentConfigHandler(YamlFile, PathObserver):

    def __init__(self, root: str):
        super().__init__(root, ExpConfigValues.CONFIG_NAME.value, ExpConfigValues.DEFAULT_DATA.value)
        self.root = root
        
    def update_path(self, path):
        self.path = path

    def create(self):
        if not (self.path == self.root):
            if not (self.get_extended_name() in os.listdir(self.path)):
                self.data = ExpConfigValues.DEFAULT_DATA.value
                self.write()
            else:
                raise FileNameAlreadyUsedError(self.get_extended_name(), self.path)
        else:
            raise FileNotAllowedInRootError(self.get_extended_name(), self.root)


    # todo
    # method overwrites old var if they have the same name
    def set_var(self, var: Variable) -> bool:
        super().read()
        to_write = var.to_dict()
        if self.data[ExpConfigValues.VARIABLES.value] is None:
            self.data[ExpConfigValues.VARIABLES.value] = to_write
        else:
            self.data[ExpConfigValues.VARIABLES.value].update(to_write)
        self.write()

        return True


    def get_vars(self) -> list[Variable]:

        old_path = self.path
        out = []
        no_overwrite = []

        while not (self.path == self.root):
            file_variables = self._get_file_vars()

            # collecting all variables from the experiment and from its parents
            for var_name in file_variables:
                if not (var_name in no_overwrite):
                    var_data = {var_name: file_variables[var_name]}
                    no_overwrite.append(var_name)
                    out.append(Variable(var_data))

            self.path = os.path.dirname(self.path)

        self.path = old_path
        return out

    def get_shortcuts(self) -> list[str]:
        self.read()
       
        return [list(i.keys()) for i in self.data[ExpConfigValues.SHORTCUTS.value]]

    def set_shortcut(self, pos, name, mapping):
        self.data[ExpConfigValues.SHORTCUTS.value][pos] = {name: mapping}

        self.write()
        
    def get_map(self, name:str) -> list:
        self.read()
        return self.data[ExpConfigValues.MAPPING.value][name]

    def has_mapping(self, name:str) -> bool:
        self.read()
      
        return name in self.data[ExpConfigValues.MAPPING.value].keys()
    
    def set_map(self, name: str, map: dict):
        self.data[ExpConfigValues.MAPPING.value][name] = map
        self.write()


    def get_shortcut_map(self, index: int) -> list:
       
        self.read()
        list_name = list(self.data[ExpConfigValues.SHORTCUTS.value][index].keys())[0]
        return self.data[ExpConfigValues.SHORTCUTS.value][index][list_name]
    
    def set_shortcut_map(self, pos: int, map: dict):
        self.read()
        list_name = list(self.data[ExpConfigValues.SHORTCUTS.value][pos].keys())[0]
        self.data[ExpConfigValues.SHORTCUTS.value][pos][list_name] = map

    def _get_file_vars(self):
        self.read()
        return self.data[ExpConfigValues.VARIABLES.value]

    def get_exp_interface(self) -> str:
        self.read()
        return self.data[ExpConfigValues.EXPERIMENT_INTERFACE.value]

    def set_exp_interface(self, exp_interface: str) -> None:
        self.read()
        self.data[ExpConfigValues.EXPERIMENT_INTERFACE.value] = exp_interface
        self.write()    

    def get_active_actionlist(self) -> str:
        self.read()
        return self.data[ExpConfigValues.ACTIVE_ACTIONLIST.value]

    def set_active_actionlist(self, action_list: str) -> None:
        self.read()
        self.data[ExpConfigValues.ACTIVE_ACTIONLIST.value] = action_list
        self.write() 

    def get_lab(self) -> str:
        self.read()
        return self.data[ExpConfigValues.LAB.value]

    def set_lab(self, lab_name: str) -> None:
        self.read()
        self.data[ExpConfigValues.LAB.value] = lab_name
        self.write()  

    def get_exp_robots(self) -> list[str]:
        self.read()
        return self.data[ExpConfigValues.EXP_ROBS.value]

    def set_exp_robot(self, robots: list[Robot]) -> None:
        self.read()
        new_robots_ip = []
        for robot in robots:
            new_robots_ip.append(robot.get_ip())
        self.data[ExpConfigValues.EXP_ROBS.value] = new_robots_ip
        self.write()

    def get_mode(self) -> str:
        self.read()
        return self.data[ExpConfigValues.MODE.value]
    
    def set_mode(self, mode: str) -> None:
        self.read()
        self.data[ExpConfigValues.MODE.value] = mode
        self.write()

    def get_position_ip(self) -> str:
        self.read()
        return self.data[ExpConfigValues.SAVE_POS_ROB.value]

    def set_position_ip(self, ip: str) -> None:
        self.read()
        self.data[ExpConfigValues.SAVE_POS_ROB.value] = ip
        self.write()

    def get_open_gripper_ip(self) -> list[str]:
        self.read()
        return self.data[ExpConfigValues.OPEN_GRIPPER_ROB.value]

    def set_open_gripper_ip(self, ip: list[str]) -> None:
        self.read()
        self.data[ExpConfigValues.OPEN_GRIPPER_ROB.value] = ip
        self.write()

    def get_close_gripper_ip(self) -> list[str]:
        self.read()
        return self.data[ExpConfigValues.CLOSE_GRIPPER_ROB.value]

    def set_close_gripper_ip(self, ip: list[str]) -> None:
        self.read()
        self.data[ExpConfigValues.CLOSE_GRIPPER_ROB.value] = ip
        self.write()

    def get_switch_gripper_ip(self) -> list[str]:
        self.read()
        return self.data[ExpConfigValues.SWITCH_GRIPPER_ROB.value]

    def set_switch_gripper_ip(self, ip: list[str]) -> None:
        self.read()
        self.data[ExpConfigValues.SWITCH_GRIPPER_ROB.value] = ip
        self.write()
    
    def get_used_space(self):
        self.read()
        return self.data[ExpConfigValues.USED_SPACE.value]

    def set_use_space(self, type):
        self.data[ExpConfigValues.USED_SPACE.value] = type
        self.write()

    def increase_shortcuts(self):
        self.read()
        self.data[ExpConfigValues.SHORTCUTS.value].append({ExpConfigValues.SHORTCUT_NAME.value: {}})
        self.write()

    def decrease_shortcuts(self):
        self.read()
        self.data[ExpConfigValues.SHORTCUTS.value].pop()
        self.write()
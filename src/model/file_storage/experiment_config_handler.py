from src.model.communication.physical.robot import Robot
from src.model.communication.position.variable import Variable
from src.model.file_storage.yaml_file import YamlFile
from src.model.file_storage.path_observer import PathObserver

import os

# todo Observer


class ExperimentConfigHandler(YamlFile, PathObserver):

    def __init__(self, root: str):
        
        self.data = {
            "experiment interface": "max",
            "active actionlist": "action",
            "number of shortcuts": 1,
            "shortcuts": [{
               "name": {}
            }],
            "mapped": {
                "alName": [[[]]],
                "alName2": [],
                },
            "lab": "labname dummy",
            "experiment robots": ["ex_ip1", "ex_ip2"],
            "mode": "test_mode",
            "save position ip": "ex_ip2",
            "open gripper ips": ["open_ip", "open_ip1"],
            "close gripper ips": ["close_ip"],
            "switch gripper ips": ["switch_ip"],
            "used space": "joint",
            "variables": {
                "example_name1": {
                    "cartesian": {
                        "coord": [10, 10, 10],
                        "quat": [10, 1, 1, 1]
                    },
                    "joint": {
                        "values": [10, 10, 10, 10, 10, 10, 10]
                    }
                }
            }
        }
        
        super().__init__(root, "experiment_config.yml", self.data)
        self.root = root
        


    def update_path(self, path):
        self.path = path

    #todo copy for sub?
    def create(self):
        if not (self.path == self.root):

            if not (self.file_name in os.listdir(self.path)):
                self.write()

            """
            elif not (self.name in os.listdir(self.path)):
                self.data1_handler.copy_file_from_parent(self.file)
                self.data1.update({"Variables": {}})
                self.__write_config()
            """

    

    # todo
    # method overwrites old var if they have the same name
    def set_var(self, var: Variable) -> bool:
        super().read()
        to_write = var.to_dict()
        if self.data["variables"] is None:
            self.data["variables"] = to_write
        else:
            self.data["variables"].update(to_write)
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
       
        return [list(i.keys())  for i in self.data["shortcuts"]]

    def set_shortcut(self, pos, name, mapping):
        
       
        
        self.data["shortcuts"][pos] = {name: mapping}

        self.write()
        


    def get_map(self, name:str) -> list:
        self.read()
        return self.data["mapped"][name]

    def has_mapping(self, name:str) -> bool:
        self.read()
      
        return name in self.data["mapped"].keys()
    
    def set_map(self, name: str, map: dict):
        self.data["mapped"][name] = map
        self.write()


    def get_shortcut_map(self, index: int) -> list:
       
        self.read()
        list_name = list(self.data["shortcuts"][index].keys())[0]
        return self.data["shortcuts"][index][list_name]
    
    def set_shortcut_map(self, pos: int, map: dict):
        self.read()
        list_name = list(self.data["shortcuts"][pos].keys())[0]
        self.data["shortcuts"][pos][list_name] = map

    def _get_file_vars(self):
        self.read()
        return self.data["variables"]

    def get_exp_interface(self) -> str:
        self.read()
        return self.data["experiment interface"]

    def set_exp_interface(self, exp_interface: str) -> None:
        self.read()
        self.data["experiment interface"] = exp_interface
        self.write()    

    def get_active_actionlist(self) -> str:
        self.read()
        return self.data["active actionlist"]

    def set_active_actionlist(self, action_list: str) -> None:
        self.read()
        self.data["active actionlist"] = action_list
        self.write() 

    def get_lab(self) -> str:
        self.read()
        return self.data["lab"]

    def set_lab(self, lab_name: str) -> None:
        self.read()
        self.data["lab"] = lab_name
        self.write()  

    def get_exp_robots(self) -> list[str]:
        self.read()
        return self.data["experiment robots"]

    def set_exp_robot(self, robots: list[Robot]) -> None:
        self.read()
        new_robots_ip = []
        for robot in robots:
            new_robots_ip.append(robot.get_ip())
        self.data["experiment robots"] = new_robots_ip
        self.write()

    def get_mode(self) -> str:
        self.read()
        return self.data["mode"]
    
    def set_mode(self, mode: str) -> None:
        self.read()
        self.data["mode"] = mode
        self.write()

    def get_position_ip(self) -> str:
        self.read()
        return self.data["save position ip"]

    def set_position_ip(self, ip: str) -> None:
        self.read()
        self.data["save position ip"] = ip
        self.write()

    def get_open_gripper_ip(self) -> list[str]:
        self.read()
        return self.data["open gripper ips"]

    def set_open_gripper_ip(self, ip: list[str]) -> None:
        self.read()
        self.data["open gripper ips"] = ip
        self.write()

    def get_close_gripper_ip(self) -> list[str]:
        self.read()
        return self.data["close gripper ips"]

    def set_close_gripper_ip(self, ip: list[str]) -> None:
        self.read()
        self.data["close gripper ips"] = ip
        self.write()

    def get_switch_gripper_ip(self) -> list[str]:
        self.read()
        return self.data["switch gripper ips"]

    def set_switch_gripper_ip(self, ip: list[str]) -> None:
        self.read()
        self.data["switch gripper ips"] = ip
        self.write()
    
    def get_used_space(self):
        self.read()
        return self.data["used space"]

    def set_use_space(self, type):
        self.data["used space"] = type
        self.write()

    def increase_shortcuts(self):
        self.read()
        self.data["shortcuts"].append({"name": {}})
        self.write()

    def decrease_shortcuts(self):
        self.read()
        self.data["shortcuts"].pop()
        self.write
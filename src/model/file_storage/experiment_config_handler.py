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
            "experiment robots": ["ex_ip1", "ex_ip2"],
            "mode": "test_mode",
            "save position ip": "save_ip",
            "open gripper ips": ["open_ip", "open_ip1"],
            "close gripper ips": ["close_ip"],
            "switch gripper ips": ["switch_ip"],
            "variables": {
                "example_name1": {
                    "used space": "joint",
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
        
        super().__init__(root, "experiment_config", self.data)
        self.root = root
        

    def update(self, path):
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
        super().read()["variables"].update({var.get_name(): var.to_dict()[var.get_name()]})
        self.write()

        return True

    def get_vars(self) -> list[Variable]:

        old_path = self.path
        out = []
        no_overwrite = []

        while not (self.path == self.root):
            file_variables = self.__get_file_vars()

            # collecting all variables from the experiment and from its parents
            for var_name in file_variables:
                if not (var_name in no_overwrite):
                    var_data = {var_name: file_variables[var_name]}
                    no_overwrite.append(var_name)
                    out.append(var_data)

            self.path = os.path.dirname(self.path)

        self.path = old_path
        return out

    def __get_file_vars(self):
        self.read()
        return super().read()["variables"]

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
        return self.data["save position robot"]

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
from src.model.communication.physical.robot import Robot
from src.model.communication.position.variable import Variable
from src.model.file_storage.yaml_file import YamlFile
from src.model.file_storage.path_observer import PathObserver

import os

# todo Observer


class ExperimentConfigHandler(YamlFile, PathObserver):

    def __init__(self, file_name: str, path: str, root: str):
        
        self.data = dict({
            "experiment interface": "max",
            "active actionlist": "action",
            "experiment robots": {
                "robot 1": "ip1",
                "robot 2": "ip2",
                "robot 3": "ip3"},

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
        })
        #self.data = dict({})
        super().__init__(path, file_name, self.data)
        self.root = root
        

    def update(self, path):
        self.path = path

    def create(self):
        if not (self.path == self.root):

            # if(self.root == os.path.dirname(self.path)):
            if not (self.file_name in os.listdir(self.path)):
                self.write()

            """
            elif not (self.name in os.listdir(self.path)):
                self.data1_handler.copy_file_from_parent(self.file)
                self.data1.update({"Variables": {}})
                self.__write_config()
            """

    def get_exp_interface(self) -> str:
        return super().read()["experiment interface"]

    def get_active_actionlist(self) -> str:
        return super().read()["active actionlist"]

    def get_robots(self) -> list[Robot]:
        all_robs = super().read()["experiment robots"]
        out = []
        for rob_data in all_robs:
            out.append(Robot(rob_data["name"], rob_data["ip"]))

        return out

    # todo
    # method overwrites old var if they have the same name
    def set_var(self, var: Variable) -> bool:
        #print("\n\n")
        #print("data")
        #print(super().read()["variables"])
        super().read()["variables"].update({var.get_name(): var.to_dict()[var.get_name()]})
        #print("\n\n")
        #print(super().read()["variables"])
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
        return super().read()["variables"]

    #TODO implement these below

    def get_save_position_robot(self) -> Robot:
        return Robot("dummy", "stupid ip")

    def get_mode(self) -> str:
        return "dummy mode"

    def next_mode(self) -> None:
        return

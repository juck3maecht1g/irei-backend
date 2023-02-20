from src.model.file_storage.yaml_file import YamlFile
from src.model.communication.physical.robot import Robot
from src.model.communication.physical.laboratory import Laboratory


import os


class GlobalConfigHandler(YamlFile):

    def __init__(self, path: str):
        data = {
            "Laboratories": {
                "Lab name": {
                    "Robots": {
                        "ex_ip1":{
                            "name": "Cooler Rob"
                        },
                       "ex_ip2": {
                            "name": "Cooler",
                        },
                        "ex_ip3": {
                            "name": "Coolr Rob",
                        }
                    },
                },
            },
            "experiment modes": ["cooler mode 1", "cooler mode 2", "test_mode"],

            "ActiveUser": "Max",
            "Users": {
                "Max": {
                    "language": "english",
                },

                "Moritz": {
                    "language": "german",
                }
            }
        }
        super().__init__(path, "global_config.yml", data)

    def create(self):
        if not (self.file_name in os.listdir(self.path)):
            self.write()

    def get_users(self) -> list[str]:
        self.read()

        return list(self.data["Users"].keys())

    def get_language(self) -> str:
        self.read()

        active_user = self.data["ActiveUser"]
        return self.data["Users"][active_user]["language"]

    def get_exp_modes(self):
        self.read()

        return self.data["experiment modes"]

    def get_labs(self) -> list[Laboratory]:
        self.read()

        lab = []

        for lab_name in self.data["Laboratories"]:
            lab.append(self.get_lab(lab_name))

        return lab

    def get_lab(self, lab_name) -> Laboratory:
        self.read()

        lab = self.data["Laboratories"][lab_name]["Robots"]
        lab_rob = []

        for rob_data in lab:
            robot = Robot(lab[rob_data]["name"], rob_data)
            lab_rob.append(robot)

        return Laboratory(lab_name, lab_rob)

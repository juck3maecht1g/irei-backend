from src.model.file_storage.yaml_file import YamlFile
from src.model.communication.physical.robot import Robot
from src.model.communication.physical.laboratory import Laboratory


import os


class GlobalConfigHandler(YamlFile):

    def __init__(self, file_name: str, path: str):
        data = {
            "Laboratories": {
                "Lab name": {
                    "Robots": {
                        "Robot1": {
                            "name": "Cooler Rob",
                            "ip": "101.10.20.101"
                        },
                        "Robot2": {
                            "name": "Cooler",
                            "ip": "101.10.0.101"
                        },
                        "Robot3": {
                            "name": "Coolr Rob",
                            "ip": "101.0.20.101"
                        }
                    }
                },
            },

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
        super().__init__(path, file_name, data)

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

        for rob_data in lab.values():
            robot = Robot(rob_data["ip"], rob_data["name"])
            lab_rob.append(robot)

        return Laboratory(lab_name, lab_rob)

from src.model.file_storage.yaml_file import YamlFile
from src.model.communication.physical.robot import Robot
from src.model.communication.physical.laboratory import Laboratory

from src.resources.config_default.global_config_values import GlobalConfigValues
from src.resources.errors.file_errors import FileNameAlreadyUsedError


import os


class GlobalConfigHandler(YamlFile):

    def __init__(self, path: str):
        super().__init__(path, GlobalConfigValues.CONFIG_NAME.value, GlobalConfigValues.DEFAULT_DATA.value)

    def create(self):
        if not (self.get_extended_name() in os.listdir(self.path)):
            self.write()
        else:
            raise FileNameAlreadyUsedError(self.get_extended_name(),self.path)

    def get_users(self) -> list[str]:
        self.read()

        return list(self.data[GlobalConfigValues.USERS.value].keys())

    def get_language(self) -> str:
        self.read()

        active_user = self.data[GlobalConfigValues.ACTIVE_USER.value]
        return self.data[GlobalConfigValues.USERS.value][active_user][GlobalConfigValues.LANGUAGE.value]

    def get_exp_modes(self):
        self.read()

        return self.data[GlobalConfigValues.EXPERIMENT_MODES.value]

    def get_labs(self) -> list[Laboratory]:
        self.read()

        lab = []

        for lab_name in self.data[GlobalConfigValues.LABS.value]:
            lab.append(self.get_lab(lab_name))

        return lab

    def get_lab(self, lab_name) -> Laboratory:
        self.read()

        lab = self.data[GlobalConfigValues.LABS][lab_name][GlobalConfigValues.ROBOTS.value]
        lab_rob = []

        for rob_data in lab:
            robot = Robot(lab[rob_data][GlobalConfigValues.NAME.value], rob_data)
            lab_rob.append(robot)

        return Laboratory(lab_name, lab_rob)

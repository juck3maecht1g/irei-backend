import unittest

from src.model.file_storage.pc_data_handler import PcDataHandler
from src.model.file_storage.action_list_handler import ActionListHandler
from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler


from src.resources.config_default.experiment_config_values import ExpConfigValues
from src.resources.errors.action_list_errors import IndexOutOfBoundsError
from src.resources.errors.file_errors import FileNotAllowedInRootError,FileNameAlreadyUsedError,FileNotExistsError

from src.root_dir import root_path

class TestSoloActionListHandler(unittest.TestCase):

    def setUp(self):
        self.pc_data = PcDataHandler(root_path)
        self.action_list = ActionListHandler(root_path)
        self.exp_config = ExperimentConfigHandler(root_path)
        self.global_config = GlobalConfigHandler(root_path)
        self.pc_data.attach(self.action_list)
        self.pc_data.attach(self.exp_config)

        self.pc_data.delete_all_content()

        if not ("global_config" in self.pc_data.get_dir_content()):
            self.global_config.create()
            for user in self.global_config.get_users():
                self.pc_data.create_directory(user)
                self.pc_data.navigate_to_child(user)
                self.exp_config.create()
                self.pc_data.navigate_to_parent()
            self.pc_data.navigate_to_child(self.global_config.get_users()[0])

    def test_get_mode(self):
        self.assertEqual(self.exp_config.get_mode(), ExpConfigValues.DEFAULT_DATA.value[ExpConfigValues.MODE.value])


if __name__ == '__main__':
    unittest.main()
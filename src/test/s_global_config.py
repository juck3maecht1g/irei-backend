import unittest

from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.model.file_storage.pc_data_handler import PcDataHandler

from src.resources.errors.file_errors import FileNameAlreadyUsedError,FileNotExistsError

from src.root_dir import root_path

import os

class TestSoloGlobalConfig(unittest.TestCase):

    def setUp(self) -> None:
        self.global_config = GlobalConfigHandler(root_path)
        pc_data = PcDataHandler(root_path)
        pc_data.delete_all_content()
        
    def test_create(self):
        self.global_config.create()
        self.assertIn(self.global_config.file_name + self.global_config.file_name_extension, os.listdir(root_path))

    def test_double_create(self):
        self.global_config.create()
        with self.assertRaises(FileNameAlreadyUsedError):
            self.global_config.create()


if __name__ == '__main__':
    unittest.main()

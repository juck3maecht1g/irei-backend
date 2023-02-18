import unittest

from src.model.file_storage.pc_data_handler import PcDataHandler
from src.model.file_storage.action_list_handler import ActionListHandler
from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.model.action.close_gripper import CloseGripper

from src.root_dir import root_path

class TestSoloActionList(unittest.TestCase):

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


    def test_create(self):
        name1 = "List1"
        name2 = "List2"
        self.action_list.create(name1, "sequential_list")
        self.action_list.create(name2, "parallel_list")
        self.assertEqual(self.action_list.get_lists(), [name1, name2])


    def test_add_action(self):
        name = "List1"
        action = CloseGripper([1])
        self.action_list.create(name, "sequential_list")
        self.action_list.add_action(name, action)
        self.assertEqual(action.nr_dictify(),self.action_list.get_list(name).nr_dictify()["content"][0])


    def test_swap_action(self):
        name = "List1"
        action1 = CloseGripper([1])
        action2 = CloseGripper([2])
        self.action_list.create(name, "sequential_list")
        self.action_list.add_action(name, action1)
        self.action_list.add_action(name, action2)
        self.action_list.swap_action(name, 0, 1)
        self.assertEqual(action2.nr_dictify(),self.action_list.get_list(name).nr_dictify()["content"][0])
        self.assertEqual(action1.nr_dictify(),self.action_list.get_list(name).nr_dictify()["content"][1])

    def test_del_action(self):
        name = "List1"
        action = CloseGripper([1])
        self.action_list.create(name, "sequential_list")
        self.action_list.add_action(name, action)
        self.assertEqual(action.nr_dictify(),self.action_list.get_list(name).nr_dictify()["content"][0])
        self.action_list.del_action(name, 0)
        self.assertEqual([], self.action_list.get_list(name).nr_dictify()["content"])
        

if __name__ == '__main__':
    unittest.main()
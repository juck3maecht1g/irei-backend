import unittest

from src.model.file_storage.pc_data_handler import PcDataHandler
from src.model.file_storage.action_list_handler import ActionListHandler
from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.model.action.close_gripper import CloseGripper
from src.model.action.action_list import ActionList

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

    def test_list_in_list(self):
        name1 = "List1"
        name2 = "List2"
        self.action_list.create(name1, "sequential_list")
        self.action_list.create(name2, "parallel_list")
        action1 = CloseGripper([0])
        action2 = CloseGripper([1])
        self.action_list.add_action(name1, action1)
        self.action_list.add_action(name2, action2)
        list2 = self.action_list.get_list(name2)
        self.action_list.add_action(name1, list2)
        self.assertEqual({'key': 'sequential_list', 'name': 'List1', 'content': [{'key': 'close_gripper', 'robots': [0],
        'robot_nrs': [0]}, {'key': 'parallel_list', 'name':'List2', 'content': [{'key': 'close_gripper', 'robots': [1],
        'robot_nrs': [1]}]}]}, self.action_list.get_list(name1).nr_dictify())
    
        

    
    #edgecases
    def test_get_lists_without_folder(self):
        self.assertEqual([], self.action_list.get_lists())

    def test_create_root(self):
        self.pc_data.navigate_to_parent()
        with self.assertRaises(ValueError):
            self.action_list.create("test", "sequential_list")

    def test_name_already_exists(self):
        name = "List1"
        self.action_list.create(name, "sequential_list")
        with self.assertRaises(ValueError):
            self.action_list.create(name, "parallel_list")

    def test_sublist_does_not_exists(self):
        name1 = "List1"
        name2 = "List2"
        self.action_list.create(name1, "sequential_list")
        unsaved_action_list = ActionList(name2, "parallel_list")
        with self.assertRaises(ValueError):
            self.action_list.add_action(name1, unsaved_action_list)

    def test_self_invocation_recursion_depth_one(self):
        name1 = "List1"
        name2 = "List2"
        self.action_list.create(name1, "sequential_list")
        list1 = self.action_list.get_list(name1)
        with self.assertRaises(ValueError):
            self.action_list.add_action(name1, list1)



    
        
    
        

if __name__ == '__main__':
    unittest.main()
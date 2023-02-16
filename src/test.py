from src.controller import irei
from src.controller.choose_lr_controller import ChooseLRController
from src.controller.control_page_controller import ControlPageController
from src.controller.fetch_for_action import FetchForAction
from src.controller.file_path_manager import FilePathManager
from src.model.file_storage.pc_data_handler import PcDataHandler
from src.model.file_storage.action_list_handler import ActionListHandler
from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.model.action.close_gripper import CloseGripper
from src.model.action.listable_factory import ListableFactory

from src.root_dir import root_path



pc_data_handler = PcDataHandler(root_path)
action_list_handler = ActionListHandler(root_path)
exp_config_handler = ExperimentConfigHandler(root_path)
global_config_handler = GlobalConfigHandler(root_path)
pc_data_handler.attach(action_list_handler)
pc_data_handler.attach(exp_config_handler)

irei._build_data_structure(pc_data_handler, global_config_handler, exp_config_handler)


ChooseLRController.set_global_config_handler(global_config_handler)
ChooseLRController.set_experiment_config_handler(exp_config_handler)

ControlPageController.set_pc_data_handler(pc_data_handler)
ControlPageController.set_exp_config_handler(exp_config_handler)
ControlPageController.set_action_list_handler(action_list_handler)
ControlPageController.set_glob_config_handler(global_config_handler)
FetchForAction.set_experiment_config_handler(exp_config_handler)
FetchForAction.set_action_list_handler(action_list_handler)
FilePathManager.set_exp_config_handler(exp_config_handler)
FilePathManager.set_pc_data_handler(pc_data_handler)

exp_config_handler = ExperimentConfigHandler(root_path)
global_config_handler = GlobalConfigHandler(root_path)
pc_data_handler.attach(action_list_handler)
pc_data_handler.attach(exp_config_handler)

if not ("global_config" in pc_data_handler.get_dir_content()):
    global_config_handler.create()
    for user in global_config_handler.get_users():
        pc_data_handler.create_directory(user)
        pc_data_handler.navigate_to_child(user)
        exp_config_handler.create()
        pc_data_handler.navigate_to_parent()



map =  exp_config_handler.get_map("some list")

print("\n\n\nmap", map, "\n\n ")



pc_data_handler.navigate_to_child("dir_from_02-16-2023_16:14:18")
FetchForAction.set_button_index()
FetchForAction.set_current_list()
FetchForAction.listable_factory = ListableFactory()
print("\n\ncreate")
print(FetchForAction.create_action_list())

print("\n\nappend")
cg1 = CloseGripper([1])
print(FetchForAction.append_action())
print("\n\ngetList")

print(action_list_handler.get_list("some list"))

print("\n\ndictify")
print("dicitfy", action_list_handler.get_list("some list").map_dictify(map))

print("\n\nnumberdictify")
print("nr dictify", action_list_handler.get_list("some list").nr_dictify())
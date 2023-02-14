from src.model.file_storage.pc_data_handler import PcDataHandler
from src.model.file_storage.action_list_handler import ActionListHandler
from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.model.action.close_gripper import CloseGripper

from src.root_dir import root_path




pc_data_handler = PcDataHandler(root_path)
action_list_handler = ActionListHandler(root_path)
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



map = {0: "ip0", "sublist": [{1: "ip1"}]}


pc_data_handler.navigate_to_child("Max")
action_list_handler.create("List1")
action_list_handler.create("List2")
cg1 = CloseGripper([1])
action_list_handler.add_action("List1", cg1)
print(action_list_handler.get_list("List1").map_dictify(map))
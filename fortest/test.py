from src.model.file_storage.pc_data_handler import PcDataHandler
from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.root_dir import root_path

global_config = GlobalConfigHandler(root_path)
exp_config = ExperimentConfigHandler(root_path)
pc_data = PcDataHandler(root_path)
pc_data.attach(exp_config)


if not ("global_config" in pc_data.get_dir_content()):
        global_config.create()
        for user in global_config.get_users():
            pc_data.create_directory(user)
            pc_data.navigate_to_child(user)
            exp_config.create()
            pc_data.navigate_to_parent()

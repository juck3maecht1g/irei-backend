from src.model.file_storage.pc_data_handler import PcDataHandler
from src.model.file_storage.action_list_handler import ActionListHandler
from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.model.alr_interface import AlrInterface

from src.controller.fetch_for_action import FetchForAction
from src.controller.choose_lr_controller import ChooseLRController
from src.controller.control_page_controller import ControlPageController
from src.controller.file_path_manager import FilePathManager
from src.controller.__init__ import app
from src.root_dir import root_path


_registered_experiments = []


@staticmethod
def _build_data_structure(pc_data: PcDataHandler, global_config: GlobalConfigHandler, exp_config: ExperimentConfigHandler) -> None:
   if not ("global_config" in pc_data.get_dir_content()):
        global_config.create()
        for user in global_config.get_users():
            pc_data.create_directory(user)
            pc_data.navigate_to_child(user)
            exp_config.create()
            pc_data.navigate_to_parent()
            

@staticmethod
def initialize() -> None:
    pc_data_handler = PcDataHandler(root_path)
    action_list_handler = ActionListHandler(root_path)
    exp_config_handler = ExperimentConfigHandler(root_path)
    global_config_handler = GlobalConfigHandler(root_path)
    pc_data_handler.attach(action_list_handler)
    pc_data_handler.attach(exp_config_handler)

    _build_data_structure(pc_data_handler, global_config_handler, exp_config_handler)


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
    app.run(debug=True, port=5000)



@staticmethod
def setup_experiment(experiment, robots) -> None:
    print("robots")
    print(robots)
    #robots = [{"name": "test"}, {"name": "test2"}]
    exp = experiment(robots)
    alr_interface = AlrInterface(exp)
    ControlPageController.set_alr_interface(alr_interface)
    FetchForAction.set_alr_interface(alr_interface)
    print("running")
  

@staticmethod
def register_experiment(experiment) -> None:
    _registered_experiments.append(experiment)



@staticmethod
def get_registered_experiments() -> list:

    return _registered_experiments

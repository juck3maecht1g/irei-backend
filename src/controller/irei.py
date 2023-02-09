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


_registered_experiments = []


@staticmethod
def initialize() -> None:
    pc_data_handler = PcDataHandler("/home/sihi/test")
    action_list_handler = ActionListHandler()
    exp_config_handler = ExperimentConfigHandler("exp_config.yml", pc_data_handler.path, pc_data_handler.root)
    global_config_handler = GlobalConfigHandler("global_config.yml", pc_data_handler.path)

    ChooseLRController.set_global_config_handler(global_config_handler)
    ChooseLRController.set_experiment_config_handler(exp_config_handler)

    ControlPageController.set_pc_data_handler(pc_data_handler)
    ControlPageController.set_exp_config_handler(exp_config_handler)
    ControlPageController.set_action_list_handler(action_list_handler)

    FetchForAction.set_experiment_config_handler(exp_config_handler)

    FilePathManager.set_pc_data_handler(pc_data_handler)
    app.run(debug=True, port=5000)


@staticmethod
def setup_experiment(experiment, robots) -> None:
    print("\n\n" "hi")
    exp = experiment(robots)
    alr_interface = AlrInterface(exp)
    
    ControlPageController.set_alr_interface(alr_interface)
    FetchForAction.set_alr_interface(alr_interface)
    alr_interface.run_exp()


@staticmethod
def register_experiment(experiment) -> None:
    _registered_experiments.append(experiment)
    print (_registered_experiments)


@staticmethod
def get_registered_experiments() -> list:
    return _registered_experiments

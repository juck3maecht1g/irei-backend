from src.model.fileStorrage.PcDataHandler import PcDataHandler
from src.model.fileStorrage.ActionListHandler import ActionListHandler
from src.model.fileStorrage.ExperimentConfigHandler import ExperimentConfigHandler
from src.model.fileStorrage.GlobalConfigHandler import GlobalConfigHandler
from src.model.alr_interface import AlrInterface

from src.controller.fetch_for_action import FetchForAction
from src.controller.choose_lr_controller import ChooseLRController
from src.controller.control_page_controller import ControlPageController
from src.controller.file_path_manager import FilePathManager
from src.controller.__init__ import app


_registered_experiments = []


@staticmethod
def initialize() -> None:
    # pc_data_handler = PcDataHandler()
    action_list_handler = ActionListHandler()
    exp_config_handler = ExperimentConfigHandler()
    global_config_handler = GlobalConfigHandler()

    # ChooseLRController.set_global_config_handler(global_config_handler)
    # ChooseLRController.set_exp_config_handler(exp_config_handler)

    # ControlPageController.set_pc_data_handler(pc_data_handler)
    ControlPageController.set_exp_config_handler(exp_config_handler)
    # ControlPageController.set_action_list_handler(action_list_handler)

    # FetchForAction.set_exp_config_handler(exp_config_handler)

    # FilePathManager.set_pc_data_handler(pc_data_handler)
    app.run(debug=True, port=5000)


@staticmethod
def setup_experiment(experiment) -> None:
    alr_interface = AlrInterface(experiment)
    ControlPageController.set_alr_interface(alr_interface)
    # fetch_for_action.set_alr_interface(alr_interface)


@staticmethod
def register_experiment(experiment) -> None:
    _registered_experiments.append(experiment)


@staticmethod
def get_registered_experiments() -> list:
    return _registered_experiments

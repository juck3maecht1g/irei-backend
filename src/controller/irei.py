from src.model.fileStorrage.PcDataHandler import PcDataHandler
from src.model.fileStorrage.ActionListHandler import ActionListHandler
from src.model.fileStorrage.ExperimentConfigHandler import ExperimentConfigHandler 
from src.model.fileStorrage.GlobalConfigHandler import GlobalConfigHandler
from src.model.alr_interface import alr_interface

from src.controller import choose_lr_controller 
from src.controller.control_page_controller import ControlPageController
from src.controller import file_path_manager 

from src.controller.__init__  import app


_registered_experiments = []

def initialize():
    #pc_data_handler = PcDataHandler()
    action_list_handler = ActionListHandler()
    experiment_config_handler = ExperimentConfigHandler()
    global_config_handler = GlobalConfigHandler()

    #choose_lr_controller.set_global_config_handler(global_config_handler)
    #choose_lr_controller.set_experiment_config_handler(experiment_config_handler)

    #control_page_controller.set_pc_data_handler(pc_data_handler)
    ControlPageController.set_experiment_config_handler(experiment_config_handler)
    #control_page_controller.set_action_list_handler(action_list_handler)

    #fetch_for_action.set_experiment_config_handler(experiment_config_handler)

    #file_path_manager.set_pc_data_handler(pc_data_handler)
    app.run(debug=True, port= 5000)

    




def setup_experiment(experiment):
    alr_interf = alr_interface(experiment)
    ControlPageController.set_alr_interface(alr_interf)
    #fetch_for_action.set_alr_interface(alr_interf)


def register_experiment(experiment):
    _registered_experiments.append(experiment)


def get_registered_experiments():
    return _registered_experiments


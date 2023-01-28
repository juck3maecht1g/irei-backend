from model.fileStorrage.FileNavigator import FileNavigator
from model.fileStorrage.ActionListHandler import ActionListHandler
from model.fileStorrage.ExperimentConfigHandler import ExperimentConfigHandler 
from model.fileStorrage.GlobalConfigHandler import GlobalConfigHandler
from model.alr_interface import alr_interface

import choose_lr_controller 
import control_page_controller
import fetch_for_action 
import file_path_manager 

from __init__ import app


_registered_experiments = []

def initialize():
    pc_data_handler = FileNavigator()
    action_list_handler = ActionListHandler()
    experiment_config_handler = ExperimentConfigHandler()
    global_config_handler = GlobalConfigHandler()

    choose_lr_controller.set_global_config_handler(global_config_handler)
    choose_lr_controller.set_experiment_config_handler(experiment_config_handler)

    control_page_controller.set_pc_data_handler(pc_data_handler)
    control_page_controller.set_experiment_config_handler(experiment_config_handler)
    control_page_controller.set_action_list_handler(action_list_handler)

    fetch_for_action.set_experiment_config_handler(experiment_config_handler)

    file_path_manager.set_pc_data_handler(pc_data_handler)

    if __name__ == "__main__":
        app.run(debug=True, port= 5000)

    




def setup_experiment(experiment):
    alr_interf = alr_interface(experiment)

    control_page_controller.set_alr_interface(alr_interf)
    fetch_for_action.set_alr_interface(alr_interf)


def register_experiment(experiment):
    _registered_experiments.append(experiment)


def get_registered_experiments():
    return _registered_experiments


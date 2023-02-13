
import json
from typing import Tuple
from flask import request
from datetime import datetime

from src.controller.__init__ import app
from src.model.alr_interface import AlrInterface
from src.model.file_storage.action_list_handler import ActionListHandler
from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.model.file_storage.pc_data_handler import PcDataHandler
from src.controller.choose_lr_controller import ChooseLRController
from datetime import datetime


class ControlPageController:
    pc_data_handler: PcDataHandler
    alr_interface: AlrInterface
    action_list_handler: ActionListHandler
    exp_config_handler: ExperimentConfigHandler
    glob_config_handler: GlobalConfigHandler

    @staticmethod
    def set_pc_data_handler(data_handler: PcDataHandler) -> None:
        ControlPageController.pc_data_handler = data_handler

    @staticmethod
    def set_alr_interface(alr_interface: AlrInterface) -> None:
        ControlPageController.alr_interface = alr_interface

    @staticmethod
    def set_exp_config_handler(exp_config_handler: ExperimentConfigHandler) -> None:
        ControlPageController.exp_config_handler = exp_config_handler

    @staticmethod
    def set_glob_config_handler(glob_config_handler: GlobalConfigHandler) -> None:
        ControlPageController.glob_config_handler = glob_config_handler

    @staticmethod
    def set_action_list_handler(action_list_handler: ActionListHandler) -> None:
        ControlPageController.action_list_handler = action_list_handler

    @staticmethod
    def get_identifier() -> str:
        return datetime.now().strftime("%m-%d-%Y_%H:%M:%S")

    marker_reset = "reset"

    @app.route("/api/" + marker_reset, methods=['POST'])
    @staticmethod
    def post_reset() -> Tuple[str, int]:
        try:
            data = request.get_json()
            if data == ControlPageController.marker_reset:
                ControlPageController.alr_interface.reset_scene()
                return 'Done', 201

            else:
                return 'marker missmatched', 201
        except Exception as e:
            return str(e)
        



    marker_start = "start"

    @app.route("/api/" + marker_start, methods=['POST'])
    @staticmethod
    def post_start() -> Tuple[str, int]:
        data = request.get_json()
        try:
            if data == ControlPageController.marker_start:
                ControlPageController.alr_interface.start_log()
                return 'Done', 201

            else:
                return 'marker missmatched', 201
        except Exception as e:
            return str(e)
    



    marker_cancel = "cancel"

    @app.route("/api/" + marker_cancel, methods=['POST'])
    @staticmethod
    def post_cancel() -> Tuple[str, int]:
        try:
            data = request.get_json()
            if data == ControlPageController.marker_cancel:
                ControlPageController.alr_interface.cancel_log()
                return 'Done', 201

            else:
                return 'marker missmatched', 201
        except Exception as e:
            return str(e)
    

    marker_stop = "stop"

    @app.route("/api/" + marker_stop, methods=['POST'])
    @staticmethod
    def post_stop() -> Tuple[str, int]:
        try:
            data = request.get_json()
            if data["marker"] == ControlPageController.marker_stop:
                result = ControlPageController.alr_interface.stop_log()
                ControlPageController.pc_data_handler.save_log(
                    result, data["name"])
                return 'Done', 201
            else:
                return 'marker missmatched', 201
        except Exception as e:
            return str(e)
    

    marker_change_gripper_state = "execchangegripper"

    # outdated execute überdenken drüber quatschen
    @app.route("/api/" + marker_change_gripper_state, methods=['POST'])
    @staticmethod
    def post_change_gripper_state() -> Tuple[str, int]:
        try:
            data = request.get_json()
            if data == ControlPageController.marker_change_gripper_state:
                robots = ControlPageController.exp_config_handler.get_switch_gripper_ip()
                ips: list[str] = []
                for robot in robots: #used if shdssdhdfsrdftzhgfklhjklödfghl
                    ips.append(robot)
                ControlPageController.alr_interface.change_gripper_state(ips)
                return 'Done', 201
            else:
                return 'marker missmatched', 201
        except Exception as e:
            return str(e)
        



        
    marker_save_position = "savePosition"

    @app.route("/api/" + marker_save_position, methods=['POST'])
    @staticmethod
    def post_save_position() -> Tuple[str, int]:
        try:
            data = request.get_json()

            if data["marker"] == ControlPageController.marker_save_position:
                result = ControlPageController.exp_config_handler.get_position_ip()
                robot = ChooseLRController.get_robots_from_ip(list(result))
                robot_dict = dict()
                robot_dict["name": robot[0].get_name(), "ip":robot[0].get_ip()]
                position = ControlPageController.alr_interface.save_posiiton(
                    result, data["name"])
                ControlPageController.exp_config_handler.set_var(position)
                return "Done", 201
            else:
                return 'marker missmatched', 201
        except Exception as e:
            return str(e)
        



    marker_cycle_modes = "cycle_modes"

    @app.route("/api/" + marker_cycle_modes, methods=['POST'])
    @staticmethod
    def post_cycle_modes() -> Tuple[str, int]:
        try:
            data = request.get_json()
            if data == ControlPageController.marker_cycle_modes:
                modes = ControlPageController.glob_config_handler.get_exp_modes()
                current_mode = ControlPageController.exp_config_handler.get_mode()
                place_of_mode = 0
                for mode in modes:
                    if modes[place_of_mode] == current_mode:
                        if place_of_mode < (len(modes) - 1):
                          
                            ControlPageController.alr_interface.set_mode(mode[place_of_mode + 1]) 
                            ControlPageController.exp_config_handler.set_mode(modes[place_of_mode + 1])
                        else : 
                              
                                ControlPageController.alr_interface.set_mode(mode[0])
                                ControlPageController.exp_config_handler.set_mode(modes[0])
                    else :
                        place_of_mode = place_of_mode + 1
                return 'Done', 201
            else:
                return 'marker missmatched', 201
        except Exception as e:
            return str(e)
        



    marker_get_mode = "get_mode"

    @app.route("/api/" + marker_get_mode)
    @staticmethod
    def get_mode() -> str:

        result = ControlPageController.exp_config_handler.get_mode()
        return json.dumps(result)

    marker_emergeny_stop = "emergency_stop"

    @app.route("/api/" + marker_emergeny_stop, methods=['POST'])
    @staticmethod
    def post_emergeny_stop() -> Tuple[str, int]:
        try:
            data = request.get_json()
            if data == ControlPageController.marker_emergeny_stop:
                ControlPageController.alr_interface.emergency_stop()
                return 'Done', 201
            else:
                return 'marker missmatched', 201
        except Exception as e:
            return str(e)
        


    marker_get_base_name_stop = "get_base_name_stop"

    @app.route("/api/" + marker_get_base_name_stop)
    @staticmethod
    def get_base_name_stop() -> str:
        return json.dumps(f"log_from_{ControlPageController.get_identifier()}")

    marker_get_base_name_save_position = "get_base_name_save_position"

    @app.route("/api/" + marker_get_base_name_save_position)
    @staticmethod
    def get_base_name_save_position() -> str:
        to_return = f"position_from_{ControlPageController.get_identifier()}"
        return json.dumps(to_return)
    
    

from src.controller.__init__ import app
from flask import request
from src.model.alr_interface import AlrInterface
from src.model.fileStorrage.action_list_handler import ActionListHandler
from src.model.fileStorrage.experiment_config_handler import ExperimentConfigHandler
from src.model.fileStorrage.pc_data_handler import PcDataHandler  
from datetime import datetime

class ControlPageController:
    pc_data_handler: PcDataHandler = None
    alr_interface: AlrInterface = None
    action_list_handler: ActionListHandler = None
    experiment_config_handler: ExperimentConfigHandler = None
    
    @staticmethod
    def  pc_data_handler(given_file_navigator):
        ControlPageController.file_navigator = given_file_navigator

    @staticmethod
    def set_alr_interface(given_alr_interface):
       ControlPageController.alr_interface = given_alr_interface

    @staticmethod
    def set_experiment_config_handler(given_experiment_config_handler):
        ControlPageController.experiment_config_handler = given_experiment_config_handler

    @staticmethod
    def set_action_list_handler(given_action_list_handler):
        ControlPageController.action_list_handler = given_action_list_handler

    @staticmethod
    def get_identifier():
        return datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
    
    marker_reset = "reset"
    @app.route("/api/" + marker_reset, methods=['POST'])
    @staticmethod
    def post_reset():
        data = request.get_json()
        if data == ControlPageController.marker_reset:
            ControlPageController.alr_interface.reset_scene()
            return 'Done', 201

        else:
            return 'failed', 201


    marker_start = "start"
    @app.route("/api/" + marker_start, methods=['POST'])
    @staticmethod
    def post_start():
        data = request.get_json()
        if data == ControlPageController.marker_start:
            ControlPageController.alr_interface.start_log()
            return 'Done', 201

        else:
            return 'failed', 201


    marker_cancel = "cancel"


    @app.route("/api/" + marker_cancel, methods=['POST'])
    @staticmethod
    def post_cancel():
        data = request.get_json()
        if data == ControlPageController.marker_cancel:
            ControlPageController.alr_interface.cancel_log()
            return 'Done', 201

        else:
            return 'failed', 201


    marker_stop = "stop"

    @app.route("/api/" + marker_stop, methods=['POST'])
    @staticmethod
    def post_stop():
        data = request.get_json()
        if data == ControlPageController.marker_stop:
            result = ControlPageController.alr_interface.stop_log()
            ControlPageController.pc_data_handler.save_log(result, data.name)
            return 'Done', 201
        else:
            return 'failed', 201


    
    marker_change_gripper_state = "execchangegripper"

    # outdated execute überdenken drüber quatschen
    @app.route("/api/" + marker_change_gripper_state, methods=['POST'])
    @staticmethod
    def post_change_gripper_state():
        data = request.get_json()
        if data == ControlPageController.marker_change_gripper_state:
            robots = ControlPageController.experiment_config_handler.get_execute_gripper()
            ips: list[str]
            for robot in robots:
                ips.append(robot.get_ip())
            ControlPageController.alr_interface.change_gripper_state(ips)
            return 'Done', 201
        else:
            return 'failed', 201


    marker_save_position = "savePosition"


    @app.route("/api/" + marker_save_position, methods=['POST'])
    @staticmethod
    def post_save_position():
        data = request.get_json()
        if data == ControlPageController.marker_save_position:
            result = ControlPageController.experiment_config_handler.get_save_position_robot()
            position = ControlPageController.alr_interface.save_posiiton(result.get_ip(), data["name"])
            ControlPageController.experiment_config_handler.add_var(position)
            return 'Done', 201
        else:
            return 'failed', 201

    marker_cycle_modes = "modes"
    @app.route("/api/" + marker_cycle_modes, methods=['POST'])
    @staticmethod
    def post_cycle_modes():
        data = request.get_json()
        if data == ControlPageController.marker_cycle_modes:
            ControlPageController.experiment_config_handler.next_mode()
            return 'Done', 201
        else:
            return 'failed', 201

    marker_get_mode = "get_mode"
    @app.route("/api/" + marker_get_mode)
    @staticmethod
    def get_mode():
        result = ControlPageController.experiment_config_handler.get_mode()
        return result

    marker_emergeny_stop = "emergency_stop"
    @app.route("/api/" + marker_emergeny_stop, methods=['POST'])
    @staticmethod
    def post_emergeny_stop():
        data = request.get_json()
        if data == ControlPageController.marker_emergeny_stop:
            ControlPageController.alr_interface.emergency_stop()
            return 'Done', 201
        else:
            return 'failed', 201
        

    marker_get_base_name_stop = "get_base_name_stop"
    @app.route("/api/" + marker_get_base_name_stop)
    @staticmethod
    def get_base_name_stop():
        return "log_from_" + ControlPageController.get_identifier()
    
    marker_get_base_name_save_position = "get_base_name_save_position"
    @app.route("/api/" +  marker_get_base_name_save_position)
    @staticmethod
    def get_base_name_save_position():
        return "position_from_" + ControlPageController.get_identifier()
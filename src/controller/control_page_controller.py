
from src.controller.__init__ import app
from flask import request
from src.model.alr_interface import alr_interface

class ControlPageController:
    file_navigator = None
    alr_interface = None
    action_list_handler = None
    experiment_config_handler = None
    
    @staticmethod
    def set_file_navigator(given_file_navigator):
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
            alr_interface.cancel_log()
            return 'Done', 201

        else:
            return 'failed', 201


    marker_stop = "stop"


    @app.route("/api/" + marker_stop, methods=['POST'])
    @staticmethod
    def post_stop():
        data = request.get_json()
        if data == ControlPageController.marker_stop:
            result = alr_interface.stop_log()
            ControlPageController.file_navigator.save_log(result)
            return 'Done', 201
        else:
            return 'failed', 201


    marker_exec_list = "executeList"


    @app.route("/api/" + marker_exec_list, methods=['POST'])
    @staticmethod
    def post_execute_list():
        data = request.get_json()
        if data == ControlPageController.marker_exec_list:
            exec_list = ControlPageController.experiment_config_handler.get_active_list
            actions = ControlPageController.action_list_handler(exec_list)
            for action in actions:
                action.execute

            return 'Done', 201
        else:
            return 'failed', 201


    marker_change_gripper_state = "execchangegripper"


    @app.route("/api/" + marker_change_gripper_state, methods=['POST'])
    @staticmethod
    def post_change_gripper_state():
        data = request.get_json()
        if data == ControlPageController.marker_change_gripper_state:
            result = ControlPageController.experiment_config_handler.get_execute_gripper()
            result.start(alr_interface)
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
            position = alr_interface.get_position(result)
            ControlPageController.experiment_config_handler.add_var(position)
            return 'Done', 201
        else:
            return 'failed', 201



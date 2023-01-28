
from src.controller.__init__ import app
from flask import request


file_navigator = None
alr_interface = None
action_list_handler = None
experiment_config_handler = None


def set_file_navigator(given_file_navigator):
    file_navigator = given_file_navigator


def set_alr_interface(given_alr_interface):
    alr_interface = given_alr_interface


def set_experiment_config_handler(given_experiment_config_handler):
    experiment_config_handler = given_experiment_config_handler


def set_action_list_handler(given_action_list_handler):
    action_list_handler = given_action_list_handler


marker_reset = "reset"


@app.route("/api/" + marker_reset, methods=['POST'])
@staticmethod
def post_reset():
    data = request.get_json()
    if data == marker_reset:
        alr_interface.reset()
        return 'Done', 201

    else:
        return 'failed', 201


marker_start = "start"


@app.route("/api/" + marker_start, methods=['POST'])
@staticmethod
def post_start():
    with open(r'src\model\testfile.txt', 'w') as f:
        f.write('start')
    data = request.get_json()
    if data == marker_start:

        alr_interface.start_logger()
        return 'Done', 201

    else:
        return 'failed', 201


marker_cancel = "cancel"


@app.route("/api/" + marker_cancel, methods=['POST'])
@staticmethod
def post_cancel():
    data = request.get_json()
    if data == marker_cancel:
        alr_interface.cancel_logger()
        return 'Done', 201

    else:
        return 'failed', 201


marker_stop = "stop"


@app.route("/api/" + marker_stop, methods=['POST'])
@staticmethod
def post_stop():
    data = request.get_json()
    if data == marker_stop:
        result = alr_interface.stop_logger()
        file_navigator.save_log(result)
        return 'Done', 201
    else:
        return 'failed', 201


marker_exec_list = "executeList"


@app.route("/api/" + marker_exec_list, methods=['POST'])
@staticmethod
def post_execute_list():
    data = request.get_json()
    if data == marker_exec_list:
        exec_list = experiment_config_handler.get_active_list
        actions = action_list_handler(exec_list)
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
    if data == marker_change_gripper_state:
        result = experiment_config_handler.get_execute_gripper()
        result.start(alr_interface)
        return 'Done', 201
    else:
        return 'failed', 201


marker_save_position = "savePosition"


@app.route("/api/" + marker_save_position, methods=['POST'])
@staticmethod
def post_save_position():
    data = request.get_json()
    if data == marker_save_position:
        result = experiment_config_handler.get_save_position_robot()
        position = alr_interface.get_position(result)
        experiment_config_handler.add_var(position)
        return 'Done', 201
    else:
        return 'failed', 201

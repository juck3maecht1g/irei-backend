from src.controller.__init__ import app
from flask import request
from src.model.communication.physical.laboratory import Lab


class ChooseLRController:
    experiment_config_handler = None
    global_config_handler = None

    current_lab = None

    @staticmethod
    def set_experiment_config_handler(given_experiment_config_handler):
        ChooseLRController.experiment_config_handler = given_experiment_config_handler

    @staticmethod
    def set_global_config_handler(given_global_config_handler):
        ChooseLRController.global_config_handler = given_global_config_handler

    lab_robots_marker = "getRobotsOfLab"

    @app.route("/api/" + lab_robots_marker)
    @staticmethod
    def get_robots_list():  # rem param
        if ChooseLRController.current_lab == None:
            return []
        to_return = []
        robots = ChooseLRController.current_lab.get_robots()
        for robot in robots:
            to_append = {"name" : robot.get_name, "ip": robot.get_ip}
            to_return.append(to_append)
        # for robot in robots:
        #    to_return.append(robot.get_ip)

        return to_return

    lab_marker = "getLab"

    @app.route("/api/" + lab_marker)
    @staticmethod
    def get_all_labs():
        data = ChooseLRController.global_config_handler.get_labs()
        to_return = dict()
        for lab in data:
            to_return[lab.get_name] = ChooseLRController.get_robots_ip_list(
                lab)
        return to_return

    current_lab_marker = "setCurrentLab"

    @app.route("/api/" + current_lab_marker, methods=['POST'])
    @staticmethod
    def set_current_lab():
        data = request.get_json()
        print(data)
        test_labs = [Lab("lab1")]
        # for lab in ChooseLRController.global_config_handler.get_labs():
        for lab in test_labs:
            if lab.get_name() == data:
                ChooseLRController.current_lab = lab
                return 'Done', 201

        return 'failed', 201

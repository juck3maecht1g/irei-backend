from typing import Tuple
from flask import request

from src.controller.__init__ import app
from src.controller.irei import get_registered_experiments, setup_experiment
from src.model.communication.physical.laboratory import Laboratory
from src.model.communication.physical.robot import Robot
from src.model.fileStorrage.GlobalConfigHandler import GlobalConfigHandler
from src.model.fileStorrage.ExperimentConfigHandler import ExperimentConfigHandler


class ChooseLRController:
    exp_config_handler: ExperimentConfigHandler
    global_config_handler: GlobalConfigHandler

    current_lab: Laboratory

    @staticmethod
    def set_exp_config_handler(exp_config_handler: ExperimentConfigHandler) -> None:
        ChooseLRController.exp_config_handler = exp_config_handler

    @staticmethod
    def set_global_config_handler(global_config_handler: GlobalConfigHandler) -> None:
        ChooseLRController.global_config_handler = global_config_handler

    lab_robots_marker = "getRobotsOfLab"

    @app.route("/api/" + lab_robots_marker)
    @staticmethod
    def get_robots_list() -> list[Robot]:
        if ChooseLRController.current_lab is None:
            return []
        to_return = []
        robots = ChooseLRController.current_lab.get_robots()
        for robot in robots:
            to_append = {"name": robot.get_name(), "ip": robot.get_ip()}
            to_return.append(to_append)

        return to_return

    lab_marker = "getLab"

    @app.route("/api/" + lab_marker)
    @staticmethod
    def get_all_labs() -> dict:
        data = ChooseLRController.global_config_handler.get_labs()
        to_return = dict()
        for lab in data:
            to_return[lab.get_name()] = ChooseLRController.get_robots_ip_list(
                lab)
        return to_return

    current_lab_marker = "setCurrentLab"

    @app.route("/api/" + current_lab_marker, methods=['POST'])
    @staticmethod
    def set_current_lab() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] == "setCurrentLab":
            for lab in ChooseLRController.global_config_handler.get_labs():
                if lab.get_name() == data["name"]:
                    ChooseLRController.current_lab = lab
                return 'Done', 201

        return 'failed', 201

    robots_exp_marker = "getRobotsInExperiment"

    @app.route("/api/" + robots_exp_marker)
    @staticmethod
    def get_robots_exp() -> dict:
        data = ChooseLRController.exp_config_handler.get_exp_robots()
        to_return = dict()
        for robot in data:
            to_append = {"name": robot.get_name(), "ip": robot.get_ip()}
            to_return.update(to_append)
        return to_return

    robots_gripper_marker = "getRobotsForGripper"

    @app.route("/api/" + robots_gripper_marker)
    @staticmethod
    def get_robots_gripper() -> dict:
        data = ChooseLRController.exp_config_handler.get_execute_gripper()
        to_return = dict()
        for robot in data:
            to_append = {"name": robot.get_name(), "ip": robot.get_ip()}
            to_return.update(to_append)
        return to_return

    reg_exp_marker = "getRegExp"

    @app.route("/api/" + reg_exp_marker)
    @staticmethod
    def get_reg_exp() -> list[str]:
        data = get_registered_experiments()
        to_return = []
        for exp in data:
            to_return.append(exp.get_name())
        return to_return

    setup_exp_marker = "setup_exp"

    @app.route("/api/" + setup_exp_marker, methods=['POST'])
    @staticmethod
    def setup_exp() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] != "SetExperiment":
            return "F", 300
        for experiment in get_registered_experiments():
            if data["experiment"] == experiment.get_name():
                setup_experiment(experiment)
            return 'Done', 201
        else:
            return 'failed', 201

    set_robots_exp_marker = "setRobotsExp"

    @app.route("/api/" + set_robots_exp_marker, methods=['POST'])
    @staticmethod
    def set_robots_exp() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] != "SetExpRobots":
            return "F", 300
        robots = []
        for ip in data["robot_ips"]:
            for robot in ChooseLRController.current_lab.get_robots():
                if ip == robot.get_ip():
                    robots.append(Robot(ip=ip, name=robot.get_name()))
        ChooseLRController.exp_config_handler.set_exp_robots(robots)
        return 'Done', 201

        # todo error condition

    set_robots_gripper_marker = "setRobotsGripper"

    @app.route("/api/" + set_robots_gripper_marker, methods=['POST'])
    @staticmethod
    def set_robots_gripper() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] != "SetChangeGripperRobots":
            return "F", 300
        robots = []
        for ip in data["robots_ips"]:
            for robot in ChooseLRController.exp_config_handler.get_exp_robots():
                if ip == robot.get_ip():
                    robots.append(Robot(ip=ip, name=robot.get_name()))
        ChooseLRController.exp_config_handler.set_execute_gripper(
            robots)
        return 'Done', 201

        # todo error condition

    # sets the robot for save position
    set_save_pos_marker = "setSavePosition"

    @app.route("/api/" + set_save_pos_marker, methods=['POST'])
    @staticmethod
    def set_save_pos() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] != "SetSavePositionRobots":
            return "F", 300
        for robot in ChooseLRController.exp_config_handler.get_exp_robots():
            if data["robot_ip"] == robot.get_ip():
                pos_robot = Robot(ip=data["robot_ip"], name=robot.get_name())
                ChooseLRController.exp_config_handler.set_save_position_robot(
                    pos_robot)
                return 'Done', 201

        return 'failed', 201

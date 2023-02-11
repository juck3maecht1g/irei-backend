from src.controller.__init__ import app
from flask import request
from src.model.communication.physical.laboratory import Laboratory
from src.model.communication.physical.robot import Robot



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
    def get_robots_list():
        if ChooseLRController.current_lab == None:
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
    def get_all_labs():
        data = ChooseLRController.global_config_handler.get_labs()
        to_return = dict()
        for lab in data:
            robots = lab.get_robots()
            robot_list = []
            for robot in robots:
                to_append = {"name": robot.get_name(), "ip": robot.get_ip()}
                robot_list.append(to_append)

            to_return[lab.get_name()] = robot_list
        return to_return

    current_lab_marker = "setCurrentLab"

    @app.route("/api/" + current_lab_marker, methods=['POST'])
    @staticmethod
    def set_current_lab():
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
    def get_robots_exp():
        data = ChooseLRController.experiment_config_handler.get_exp_robots()
        to_return = []
        for robot in data:
            to_append = {"name": robot.get_name, "ip": robot.get_ip}
            to_return.append(to_append)
        return to_return

    robots_gripper_marker = "getRobotsForGripper"

    @app.route("/api/" + robots_gripper_marker)
    @staticmethod
    def get_robots_gripper():
        data = ChooseLRController.experiment_config_handler.get_execute_gripper()
        to_return = []
        for robot in data:
            to_append = {"name": robot.get_name, "ip": robot.get_ip}
            to_return.append(to_append)
        return to_return

    reg_exp_marker = "getRegExp"

    @app.route("/api/" + reg_exp_marker)
    @staticmethod
    def get_reg_exp():
        from src.controller.irei import get_registered_experiments
        data = get_registered_experiments()
        to_return = []
        for exp in data:
            to_return.append(exp.get_name())
        return to_return

    setup_exp_marker = "setup_exp"

    @app.route("/api/" + setup_exp_marker, methods=['POST'])
    @staticmethod
    def setup_exp():
        from src.controller.irei import get_registered_experiments, setup_experiment
        data = request.get_json()
        
        if data["marker"] != "SetExperiment":
            
            return "F", 300
        for experiment in get_registered_experiments():
            print("\n\n")
            print(experiment.get_name())
            if data["experiment"] == experiment.get_name():
                robots = ChooseLRController.get_robots_exp()
                
                setup_experiment(experiment, robots)
            return 'Done', 201
        else:
            
            return 'failed', 201

    set_robots_exp_marker = "setRobotsExp"

    @app.route("/api/" + set_robots_exp_marker, methods=['POST'])
    @staticmethod
    def set_robots_exp():
        data = request.get_json()
        if data["marker"] != "SetExpRobots":
            return "F", 300
        robots = []
        for ip in data["robot_ips"]:
            for robot in ChooseLRController.current_lab.get_robots():
                if ip == robot.get_ip():
                    robots.append(Robot(ip=ip, name=robot.get_name()))
        ChooseLRController.experiment_config_handler.set_exp_robots(robots)
        return 'Done', 201

        # todo error condition

    set_robots_gripper_marker = "setRobotsGripper"

    @app.route("/api/" + set_robots_gripper_marker, methods=['POST'])
    @staticmethod
    def set_robots_gripper():
        data = request.get_json()
        if data["marker"]!= "SetChangeGripperRobots":
            return "F", 300
        robots = []
        for ip in data["robot_ips"]:
            for robot in ChooseLRController.experiment_config_handler.get_exp_robots():
                if ip == robot.get_ip():
                    robots.append(Robot(ip=ip, name=robot.get_name()))
        ChooseLRController.experiment_config_handler.set_execute_gripper(
            robots)
        return 'Done', 201

        # todo error condition

    # sets the robot for save position
    set_save_pos_marker = "setSavePosition"

    @app.route("/api/" + set_save_pos_marker, methods=['POST'])
    @staticmethod
    def set_save_pos():
        data = request.get_json()
        if data["marker"] != "SetSavePositionRobots":
            return "F", 300
        for robot in ChooseLRController.experiment_config_handler.get_exp_robots():
            if data["robot_ip"] == robot.get_ip():
                pos_robot = Robot(ip=data.robot_ip, name=robot.get_name())
                ChooseLRController.experiment_config_handler.set_save_position_robot(
                    pos_robot)
                return 'Done', 201

        return 'failed', 201

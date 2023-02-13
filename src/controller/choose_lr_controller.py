from src.controller.__init__ import app
from flask import request
from src.model.communication.physical.laboratory import Laboratory
from src.model.communication.physical.robot import Robot



class ChooseLRController:

    experiment_config_handler = None
    global_config_handler = None


    active_experiment = False
    current_lab = None

    @staticmethod
    def set_experiment_config_handler(given_experiment_config_handler):
        ChooseLRController.experiment_config_handler = given_experiment_config_handler

    @staticmethod
    def set_global_config_handler(given_global_config_handler):
        ChooseLRController.global_config_handler = given_global_config_handler



    @staticmethod
    def get_robots_from_ip(ips: list[str]):
            all_robots = ChooseLRController.current_lab.get_robots()
            robots = [Robot]
            for ip in ips:
                for robot in all_robots:
                    if ip == robot.get_ip():
                        robots.append(robot)
            return robots

   




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

        to_return = []
        for lab in data:
            lab_dict = dict()
            lab_dict["name"] = lab.get_name()
            robots = lab.get_robots()
            robot_list = []
            for robot in robots:
                to_append = {"name": robot.get_name(), "ip": robot.get_ip()}
                robot_list.append(to_append)
            lab_dict["robots"] = robot_list
            to_return.append(lab_dict)
        return to_return

    current_lab_marker = "setCurrentLab"

    @app.route("/api/" + current_lab_marker, methods=['POST'])
    @staticmethod
    def set_current_lab():
        try:
            data = request.get_json()
            if data["marker"] == "setCurrentLab":
    

                for lab in ChooseLRController.global_config_handler.get_labs():
        
                    if lab.get_name() == data["name"]:
                        ChooseLRController.current_lab = lab
            
                        return 'Done', 201

            return 'marker missmatched', 201
        except Exception as e:
            return str(e)
        



    robots_exp_marker = "getRobotsInExperiment"

    @app.route("/api/" + robots_exp_marker)
    @staticmethod
    def get_robots_exp():
        data = ChooseLRController.experiment_config_handler.get_exp_robots()
        robots = ChooseLRController.current_lab.get_robots()
        to_return = []
        for ip in data:
            for robot in robots:
                if robot.get_ip == ip:
                    to_append = {"name": robots.get_name, "ip": robot.get_ip}
                    to_return.append(to_append)
        return to_return

    robots_gripper_marker = "getRobotsForGripper"

    @app.route("/api/" + robots_gripper_marker)
    @staticmethod
    def get_robots_gripper():
        to_return = []
        for robot in ChooseLRController.get_robots_from_ip(ChooseLRController.experiment_config_handler.get_switch_gripper_ip()):
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



    set_robots_exp_marker = "setRobotsExp"

    @app.route("/api/" + set_robots_exp_marker, methods=['POST'])
    @staticmethod
    def set_robots_exp():
        try:
            data = request.get_json()
    
            if data["marker"] != "setExpRobots":
                return data["marker"], 201
            robots = []
            for ip in data["robot_ips"]:
                for robot in ChooseLRController.current_lab.get_robots():
                    if ip == robot.get_ip():
                        robots.append(Robot(ip=ip, name=robot.get_name()))
            ChooseLRController.experiment_config_handler.set_exp_robot(robots)
            return 'Done', 201
        except Exception as e:
            return str(e)














    @staticmethod
    def setup_exp_from_name(name):
        from src.controller.irei import get_registered_experiments, setup_experiment
        print("\n\ntest")
        test = get_registered_experiments()
        try:   
            for experiment in test:
                print("\n\n"+ experiment.get_name())
                if name == experiment.get_name():

                    robots = ChooseLRController.get_robots_exp()
                    #setup_experiment(experiment, robots)
                    return "Done"
       
        except Exception as e:
            
            return str(e)
       





















    setup_exp_marker = "setup_exp"

    @app.route("/api/" + setup_exp_marker, methods=['POST'])
    @staticmethod
    def setup_exp():
        try:
            data = request.get_json() 
            print("\n\n" +data["marker"])
            if data["marker"] == "SetExperiment":
                text = ChooseLRController.setup_exp_from_name(data["experiment"])
                if text == "Done":
                    ChooseLRController.experiment_config_handler.set_exp_interface(data["experiment"])
                    return "Done", 201
                else :
                    return "could not set up experiment", 201
            else :
                return 'marker missmatched', 201   
        except Exception as e:
           
            return str(e)

   
        



    set_robots_gripper_marker = "setRobotsGripper"

    @app.route("/api/" + set_robots_gripper_marker, methods=['POST'])
    @staticmethod
    def set_robots_gripper():
        try:
            data = request.get_json()
            if data["marker"]!= "SetChangeGripperRobots":
                return "F", 300
            robots = []
            for ip in data["robot_ips"]:
                  for robot in ChooseLRController.get_robots_from_ip(ChooseLRController.experiment_config_handler.get_exp_robots()):
                    if ip == robot.get_ip():
                        robots.append(ip) #Robot(ip=ip, name=robot.get_name()) for implementation with robots not strings
            ChooseLRController.experiment_config_handler.set_switch_gripper_ip(
                robots)
            return 'Done', 201
        except Exception as e:
            return str(e)

    # sets the robot for save position
    set_save_pos_marker = "setSavePosition"

    @app.route("/api/" + set_save_pos_marker, methods=['POST'])
    @staticmethod
    def set_save_pos():
        try:
            data = request.get_json()
            if data["marker"] != "SetSavePositionRobots":
                return "F", 300
            for robot in ChooseLRController.get_robots_from_ip(ChooseLRController.experiment_config_handler.get_exp_robots()):
                if data["robot_ip"] == robot.get_ip():
                    pos_robot = Robot(ip=data.robot_ip, name=robot.get_name())
                    ChooseLRController.experiment_config_handler.set_position_ip(
                       pos_robot.get_ip())
                    return 'Done', 201
        except Exception as e:
            return str(e)


    @app.route("/api/confirm_dir_coise", methods=['POST'])
    @staticmethod
    def confirm_dir_coise():
        #try :
            valid = False
            data = request.get_json()
            if data != "confirm_dir_coise":
                return 'marker missmatched',201
        
            lab_name = ChooseLRController.experiment_config_handler.get_lab()
            for lab in ChooseLRController.global_config_handler.get_labs():
               
                if lab_name == lab.get_name():
                    
                    ChooseLRController.current_lab = lab
                    valid = True

            if not valid :
                return "something is wrong with the chosen lab in this folder", 201
     
            exp_name = ChooseLRController.experiment_config_handler.get_exp_interface()
            print("\n\n"+ exp_name)
            if ChooseLRController.setup_exp_from_name(exp_name):
                return "Done", 201
            else :
                ChooseLRController.active_experiment = False
                return "the experiment registered in this folder could not be run", 201
        #except Exception as e:
            return str(e)


    """
    this method return if there is an experiment active at the moment
    """
    is_exp_active_marker = "is_exp_active"

    @app.route("/api/" + is_exp_active_marker)
    @staticmethod
    def is_exp_active():
        if ChooseLRController.active_experiment:
            return "true"
        else:
            return "false"
  



   
from src.controller.__init__ import app

experiment_config_handler = None
global_config_handler = None

@staticmethod
def set_experiment_config_handler(given_experiment_config_handler):
        experiment_config_handler = given_experiment_config_handler

@staticmethod
def set_global_config_handler(given_global_config_handler):
        global_config_handler = given_global_config_handler

lab_marker = "getLab"
@app.route("/api/" + lab_marker)
@staticmethod
def getLab(): 
    data =global_config_handler.get_lab()
    toreturn = dict()
    for lab in data:
           toreturn[lab.get_name] = __get_robots_ip_list(lab)
    return toreturn




@staticmethod
def __get_robots_ip_list(lab) :
    toreturn = []
    robots = lab.get_robots()
    for robot in robots:
              toreturn.append(robot.get_ip)
        
    return toreturn
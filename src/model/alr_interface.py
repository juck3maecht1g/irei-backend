from src.model.communication.position.variable import Variable


class AlrInterface:
    # cunstruktor
    active_experiment = None

    def __init__(self, active_experiment):
        self.active_experiment = active_experiment
        #self.active_experiment = active_experiment

    def start_log(self):
        # self.active_experiment.start_log()
        print("start")

    def cancel_log(self):
        # self.active_experiment.cancel_log()
        print("logging canceled")

    def stop_log():
        # self.active_experiment.stop_log()
        print("stop")
        return {"log1": "234715623478568127"}  # to be deleted

    def reset_scene(self):
        # self.active_experiment.reset()
        print("scene reset")

    # maby delete those methods

    def wait(self, robot, time):
        self.active_experiment.wait(robot, time)

    def open_gripper(self, robot):
        self.active_experiment.open_gripper(robot)

    def close_gripper(self, robot):
        self.active_experiment.close_gripper(robot)

    # depending on how coordinates are served
    def approach_position(self, robot, position, is_cartesian):
        if is_cartesian:
            self.active_experiment.approach_cartesian(
                robot, position.get_cartesian)
        else:
            self.active_experiment.approach_joint(robot, position.get_joint)

    def save_posiiton(self, robot, name):
        cartesian = self.get_cartesian_position_of(robot)
        joint = self.get_joint_position_of(robot)
        position = Variable(cartesian, joint)
        print("saved position in alr-sim")
        return Variable(dict({name: dict({
                    "used space": "joint",
                    "cartesian": {
                        "coord": [15, 15, 15],
                        "quat": [10, 1, 1, 1]
                    },
                    "joint": {
                        "values": [105, 150, 150, 10, 150, 10, 10]
                    }
                })}))

    def emergency_stop(self):
        self.active_experiment.emergency_stop()
        print("emergency")

    def set_mode(self, mode):
        self.active_experiment.set_mode(mode)
        print("sets the experiment in the specified mode")

    def execute_sequenzial_list(self, action_list_dict: dict):
        self.active_experiment.execute_sequenzial_list(action_list_dict)
        print("would exec list")

    def validate_action(self, action: dict) -> bool:
         print("would test the action")
         return self.active_experiment.validate_action(dict)
       

    def change_gripper_state(self, robots: list[dict]):
        print("would change state of all chosen gripppers")
        return self.active_experiment.change_grippper_state(robots)
        

    def run_exp(self):
        print( self.active_exp.run())
        
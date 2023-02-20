from src.model.communication.position.variable import Variable


class AlrInterface:
    # cunstruktor

    def __init__(self, active_experiment):
        self.active_experiment = active_experiment
 

    def start_log(self):
        self.active_experiment.start_log()
        print("start")

    def cancel_log(self):
        self.active_experiment.cancel_log()
        print("logging canceled")

    def stop_log(self):
        print("stop log")
        to_return = self.active_experiment.stop_log()
        #print(to_return)
        return to_return  # to be deleted

    def reset_scene(self):
        self.active_experiment.reset()
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
        print("saving") #[0.2,0.2,0.2,0.2,0.2,0,0]
        print(self.active_experiment)
        cartesian = self.active_experiment.get_cartesian_position_of(robot)
        print("CART", cartesian)
        joint = self.active_experiment.get_joint_position_of(robot)
        cart_dict = {"coord": cartesian, "quat": [1, 0, 0, 0]} # test
        joint_dict = {"values": joint}
        var_dict = {name: {"used space": "joint", "cartesian": cart_dict, "joint": joint_dict}}
        print("CREATE VAR")
        position = Variable(var_dict)
        print("saved position in alr-sim")
        print(joint)
        # return Variable(dict({name: dict({
        #             "used space": "joint",
        #             "cartesian": {
        #                 "coord": [15, 15, 15],
        #                 "quat": [10, 1, 1, 1]
        #             },
        #             "joint": {
        #                 "values": [105, 150, 150, 10, 150, 10, 10]
        #             }
        #         })}))
        return position

    def emergency_stop(self):
        self.active_experiment.emergency_stop()
        print("emergency")

    def set_mode(self, mode):
        self.active_experiment.set_mode(mode)
        print("sets the experiment in the specified mode")

    def execute_list(self, action_list_dict: dict):
        self.active_experiment.execute_list(action_list_dict)
        print("would exec list")

    def validate_action(self, action: dict) -> bool:
         print("would test the action")
         return self.active_experiment.validate_action(action)
       

    def change_gripper_state(self, robot, robots: list[str]):
        print("would change state of all chosen gripppers")
        return self.active_experiment.change_grippper_state(robot, robots)
        

    def run_exp(self):
        print("todo")
        print(self.active_experiment)
        self.active_experiment.run()
        
class alr_interface:
    #cunstruktor
    active_experiment = None

    def __init__(self, active_experiment):
        self.active_experiment = active_experiment

    def start_log(self):
        self.active_experiment.start_log()

    def cancel_log(self):
        self.active_experiment.cancel_log()
        
    def stop_log(self):
        return self.active_experiment.stop_log()
    
    def reset_scene(self):
        self.active_experiment.reset()

   
    def wait(self, ip, time):
        self.active_experiment.wait(ip, time)

    def open_gripper(self, ip):
        self.active_experiment.open_gripper(ip)   

    def close_gripper(self, ip):
        self.active_experiment.close_gripper(ip)   

    def approach_position(self, ip, position, is_cartesian):
        if is_cartesian:
            self.active_experiment.approach_cartesian(ip, position.get_cartesian)
        else: self.active_experiment.approach_joint(ip, position.get_joint)

    def save_posiiton(self, ip):
        cartesian = self.get_cartesian_position_of(ip)
        joint = self.get_joint_position_of(ip)
        position = position(cartesian, joint)

        return position
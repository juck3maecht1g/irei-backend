from src.model.communication.position.position import Position

class alr_interface:
    #cunstruktor
    active_experiment = None

    def __init__(self, active_experiment):
        self.active_experiment = active_experiment
        #self.active_experiment = active_experiment

    def start_log(self):
        #self.active_experiment.start_log()
        print("start")

    def cancel_log(self):
        #self.active_experiment.cancel_log()
        print("logging canceled")
        
    def stop_log():
         #self.active_experiment.stop_log()
         print("stop")
         return {"log1": "234715623478568127"} # to be deleted
    
    def reset_scene(self):
        #self.active_experiment.reset()
        print("scene reset")
   


    # maby delete those methods
    def wait(self, ip, time):
        self.active_experiment.wait(ip, time)

    def open_gripper(self, ip):
        self.active_experiment.open_gripper(ip)   

    def close_gripper(self, ip):
        self.active_experiment.close_gripper(ip)   

    def approach_position(self, ip, position, is_cartesian): # depending on how coordinates are served
        if is_cartesian:
            self.active_experiment.approach_cartesian(ip, position.get_cartesian)
        else: self.active_experiment.approach_joint(ip, position.get_joint)

    def save_posiiton(self, ip):
        #cartesian = self.get_cartesian_position_of(ip)
        #joint = self.get_joint_position_of(ip)
        #position = Position(cartesian, joint)
        print("saved position in alr-sim")
        return {"wanttobePosition": "asdghlfgjsdkjfh"}
    
    def emergency_stop(self):
        #self.active_experiment.emergency_stop()
        print("experiment doew what ever is implemented for an emergency stop")

    def set_mode(self, mode):
        #self.active_experiment.set_mode(mode)
        print("sets the experiment in the specified mode")

    def execute_sequenzial_list(self, action_list_dict: dict):
        #self.active_experiment.execute_sequenzial_list(action_list_dict)
        print("would exec list")


    def validate_action(self,action:dict)-> bool:
        #return self.active_experiment.validate_action(dict)
        print("would test the action")

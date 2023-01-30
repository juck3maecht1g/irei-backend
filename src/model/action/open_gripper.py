

class OpenGripper:
    key :str = "open_gripper"
    chosen_robot :str

    def __init__ (self, robot_nr :str): 
        self.chosen_robot = robot_nr
      



    def get_chosen_robot(self):
        return self.chosen_robot
    


    def dictify (self, ip:str):
        to_return = dict()
        to_return["key"] = self.key
        to_return["ip"] = ip
        return to_return
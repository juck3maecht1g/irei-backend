

class OpenGripper:
    key :str = "open_gripper"
    #chosen_robot :str

    def __init__ (self, robot_nr :str): 
        self.key = OpenGripper.key
        self.chosen_robot = robot_nr
      



    def get_chosen_robot(self):
        return self.chosen_robot
    


    def dictify (self):
        to_return = dict()
        to_return["key"] = self.key
        to_return["chosen_robot"] = self.chosen_robot
        return to_return




class CustomAction:
    key :str = "custom"
    #chosen_robot :str
    #chosen_action: str

    def __init__ (self, robot_nr :str, action:str): 
        self.key = CustomAction.key
        self.chosen_robot = robot_nr
        self.chosen_action = action



    def get_chosen_robot(self):
        return self.chosen_robot
    


    def dictify (self):
        to_return = dict()
        to_return["key"] = self.key
        to_return["chosen_robot"] = self.chosen_robot
        to_return["custom_action"] = self.chosen_action
        return to_return
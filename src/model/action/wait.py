

class Wait:
    key :str = "wait"
    chosen_robot :str
    chosen_time: str

    def __init__ (self, robot_nr :str, time:str): 
        self.chosen_robot = robot_nr
        self.chosen_time= time



    def get_chosen_robot(self):
        return self.chosen_robot
    


    def dictify (self, ip:str):
        to_return = dict()
        to_return["key"] = self.key
        to_return["ip"] = ip
        to_return["chosen_time"] = self.chosen_time
        return to_return



class MoveToPosition:
    key :str = "move"
    chosen_robot :str
    coordinates: dict
    is_cartesian: bool

    def __init__ (self, robot_nr :str, coordinates: dict, is_cartesian:bool): 
        self.chosen_robot = robot_nr
        self.coordinates = coordinates
        self.is_cartesian = is_cartesian



    def get_chosen_robot(self):
        return self.chosen_robot
    


    def dictify (self, ip:str):
        to_return = dict()
        to_return["key"] = self.key
        to_return["ip"] = ip
        to_return["is_cartesina"] = self.is_cartesian
        to_return["coorsiantes"] = self.coordinates
        return to_return
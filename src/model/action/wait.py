from src.model.action.listable_action import ListableAction


class Wait(ListableAction):
    key: str = "wait"

    def __init__(self, robot_nr: int, time: int) -> None: 
        self.key = Wait.key
        self.robot_nr = robot_nr
        self.time = time



    def get_robot_nr(self) -> int:
        return self.robot_nr
    


    def dictify(self) -> dict:
        to_return = dict()
        to_return["key"] = self.key
        to_return["robot_nr"] = self.robot_nr
        to_return["time"] = self.time
        return to_return
